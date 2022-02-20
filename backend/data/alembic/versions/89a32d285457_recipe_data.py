"""recipe data

Revision ID: 89a32d285457
Revises: 157e941a0231
Create Date: 2022-02-19 18:27:02.602889

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from copy import deepcopy


# revision identifiers, used by Alembic.
revision = '89a32d285457'
down_revision = '157e941a0231'
branch_labels = None
depends_on = '157e941a0231'

try:
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    metadata = sa.schema.MetaData(bind=bind)
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
except NameError:
    pass

recipe_datum = []
recipe_datum.append({
        'name': 'Lasanha de Carne Moída',
        'description': 'Uma Lasanha de Carne Moída',
        'ingredient': [
            {
                'name': 'Massa de Lasanha',
                'amount': 250,
                'amount_unit': 'g'
            },
            {
                'name': 'Carne Moída',
                'amount': 500,
                'amount_unit': 'g'
            },
            {
                'name': 'Molho de Tomate',
                'amount': 240,
                'amount_unit': 'g'
            },
            ],
        })

def upgrade():
    def upgrade_ingredient(ingredient_x_recipe_datum, recipe_id):
        for ingredient_x_recipe_data in ingredient_x_recipe_datum:
            ingredient_x_recipe_data = deepcopy(ingredient_x_recipe_data)
            ingredient_x_recipe_data['recipe_id'] = recipe_id
            ingredient_data = {'name': ingredient_x_recipe_data['name']}
            del ingredient_x_recipe_data['name']
            try:
                ret = session.execute(
                        sa.insert(ingredient).
                        values(ingredient_data).
                        returning(ingredient.c.id)
                        )
                [ingredient_id] = ret.fetchone()
            except sa.exc.IntegrityError:
                ret = session.execute(
                        sa.select(ingredient).
                        where(ingredient.c.name == ingredient_data['name'])
                        )
                [ingredient_id] = ret.fetchone()
            ingredient_x_recipe_data['ingredient_id'] = ingredient_id
            ret = session.execute(
                    sa.insert(ingredient_x_recipe).
                    values(ingredient_x_recipe_data)
                    )

    for recipe_data in recipe_datum:
        recipe_data = deepcopy(recipe_data)
        ingredient_x_recipe_datum = []
        if 'ingredient' in recipe_data:
            ingredient_x_recipe_datum = deepcopy(recipe_data['ingredient'])
            del recipe_data['ingredient']
        ret = session.execute(
                sa.insert(recipe).values(recipe_data).
                returning(recipe.c.id)
                )
        [recipe_id] = ret.fetchone()
        upgrade_ingredient(ingredient_x_recipe_datum, recipe_id)



def downgrade():
    def downgrade_ingredient(ingredient_x_recipe_datum, recipe_id):
        for ingredient_x_recipe_data in ingredient_x_recipe_datum:
            ingredient_x_recipe_data = deepcopy(ingredient_x_recipe_data)
            ingredient_x_recipe_data['recipe_id'] = recipe_id
            ingredient_data = {'name': ingredient_x_recipe_data['name']}
            del ingredient_x_recipe_data['name']
            ret = session.execute(
                    sa.select(ingredient.c.id).
                    where(ingredient.c.name == ingredient_data['name'])
                    )
            [ingredient_id] = ret.fetchone()
            ingredient_x_recipe_data['ingredient_id'] = ingredient_id
            op.execute(
                    ingredient_x_recipe.delete().
                    where(
                        ingredient_x_recipe.c.recipe_id
                            == ingredient_x_recipe_data['recipe_id']
                        and ingredient_x_recipe.c.ingredient_id
                            == ingredient_x_recipe_data['ingredient_id']
                        )
                    )
            try:
                op.execute(
                        ingredient.delete().
                        where(
                            ingredient.c.id == ingredient_id
                            )
                        )
            except sa.exc.IntegrityError:
                pass
        
    for recipe_data in recipe_datum:
        recipe_data = deepcopy(recipe_data)
        ingredient_x_recipe_datum = []
        if 'ingredient' in recipe_data:
            ingredient_x_recipe_datum = deepcopy(recipe_data['ingredient'])
            del recipe_data['ingredient']
        ret = session.execute(
                sa.select(recipe.c.id).
                where(recipe.c.name == recipe_data['name'])
                )
        [recipe_id] = ret.fetchone()
        downgrade_ingredient(ingredient_x_recipe_datum, recipe_id)
        op.execute(
                recipe.delete().
                where(recipe.c.name == recipe_data['name'])
                )

