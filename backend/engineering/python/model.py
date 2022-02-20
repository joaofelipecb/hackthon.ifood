import sqlalchemy as sa

metadata = sa.MetaData()

recipe = sa.Table(
        'recipe',
        metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('description', sa.Unicode(500)),
        )

ingredient = sa.Table(
        'ingredient',
        metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(200), nullable=False),
        )

ingredient_x_recipe = sa.Table(
        'ingredient_x_recipe',
        metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('recipe_id', sa.Integer, sa.ForeignKey('recipe.id'), nullable=False),
        sa.Column('ingredient_id', sa.Integer, sa.ForeignKey('ingredient.id'), nullable=False),
        sa.Column('amount', sa.Float, nullable=False),
        sa.Column('amount_unit', sa.String(20), nullable=False),
        )

def get_ingredients_by_recipe_name(engine, recipe_name):
    with engine.connect() as connection:
        ret = connection.execute(
            sa.select(ingredient).
                join(ingredient_x_recipe,
                    ingredient.c.id ==
                        ingredient_x_recipe.c.ingredient_id).
                join(recipe,
                    ingredient_x_recipe.c.recipe_id ==
                        recipe.c.id).
                where(recipe.c.name == recipe_name)
            )
        result = [
                    {'id': row[0], 'name': row[1]}
                    for row in list(ret.fetchall())
                 ]
        return result

product = sa.Table(
        'product',
        metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('image', sa.String(200), nullable=False),
        sa.Column('amount', sa.Float, nullable=False),
        sa.Column('amount_unit', sa.String(20), nullable=False),
        sa.Column('vegetarian', sa.Boolean, nullable=False),
        sa.Column('vegan', sa.Boolean, nullable=False),
        sa.Column('diet', sa.Boolean, nullable=False),
        sa.Column('light', sa.Boolean, nullable=False),
        sa.Column('lactose_free', sa.Boolean, nullable=False),
        sa.Column('gluten_free', sa.Boolean, nullable=False),
        )

ai_similarity_ingredient_x_product_default = sa.Table(
        'ai_similarity_ingredient_x_product_default',
        metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('ingredient_id', sa.Integer, sa.ForeignKey('ingredient.id'), nullable=False),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id'), nullable=False),
        sa.Column('score', sa.Float, nullable=False),
        )

def get_product_recomendation_by_ingredient_id(engine, ingredient_id):
    with engine.connect() as connection:
        ret = connection.execute(
                sa.select(
                    product.c.id,
                    product.c.name,
                    product.c.image,
                    ai_similarity_ingredient_x_product_default.c.score
                    ).
                select_from(
                    sa.join(
                        product,
                        ai_similarity_ingredient_x_product_default,
                        product.c.id ==
                            ai_similarity_ingredient_x_product_default.c.id
                            )
                    ).
                where(
                    ai_similarity_ingredient_x_product_default.c.
                        ingredient_id == ingredient_id
                    ).
                order_by(
                    ai_similarity_ingredient_x_product_default.c.score.desc()
                    )
                )
        result = [
                {
                    'id': row[0],
                    'name': row[1],
                    'image': row[2],
                    'score': row[3]
                }
                for row in ret
                ]
        return result
