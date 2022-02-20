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

def get_product_recomendation_by_ingredient_id(engine, ingredient_id, restrictions):
    def include_restrictions_filter(filter_, restrictions):
        for restriction in restrictions:
            if restriction == 'vegetarian':
                filter_ = sa.sql.and_(filter_, (product.c.vegetarian == True))
            elif restriction == 'vegan':
                filter_ = sa.sql.and_(filter_, (product.c.vegan == True))
            elif restriction == 'diet':
                filter_ = sa.sql.and_(filter_, (product.c.diet == True))
            elif restriction == 'light':
                filter_ = sa.sql.and_(filter_, (product.c.light == True))
            elif restriction == 'lactose_free':
                filter_ = sa.sql.and_(filter_, (product.c.lactose_free == True))
            elif restriction == 'gluten_free':
                filter_ = sa.sql.and_(filter_, (product.c.gluten_free == True))
        return filter_

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
                    include_restrictions_filter(
                        ai_similarity_ingredient_x_product_default.c.
                            ingredient_id == ingredient_id,
                        restrictions
                        )
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
                    'score': row[3],
                }
                for row in ret
                ]
        return result
