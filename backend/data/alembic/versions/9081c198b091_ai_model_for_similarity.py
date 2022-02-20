"""ai model for similarity

Revision ID: 9081c198b091
Revises: 3b66497958b1
Create Date: 2022-02-19 23:07:12.100062

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from copy import deepcopy


# revision identifiers, used by Alembic.
revision = '9081c198b091'
down_revision = '3b66497958b1'
branch_labels = None
depends_on = '3b66497958b1'

try:
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    metadata = sa.schema.MetaData(bind=bind)

    ingredient = sa.Table(
            'ingredient',
            metadata,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(200), nullable=False),
            )

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

    ingredient_x_product = sa.Table(
            'ai_similarity_ingredient_x_product_default',
            metadata,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('ingredient_id', sa.Integer, sa.ForeignKey('ingredient.id'), nullable=False),
            sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id'), nullable=False),
            sa.Column('score', sa.Float, nullable=False),
            )

except NameError:
    pass

ingredient_x_product_datum = []
ingredient_x_product_datum.append({
    'ingredient': 'Massa de Lasanha',
    'product': 'Massa Para Lasanha Renata',
    'score': 0.85,
    })

ingredient_x_product_datum.append({
    'ingredient': 'Massa de Lasanha',
    'product': 'Massa Fresca Para Lasanha Caue',
    'score': 0.92,
    })

ingredient_x_product_datum.append({
    'ingredient': 'Massa de Lasanha',
    'product': 'Lasanha Massa Vitarella',
    'score': 0.52,
    })

ingredient_x_product_datum.append({
    'ingredient': 'Massa de Lasanha',
    'product': 'Massa para Lasanha e Canelone DA BOA',
    'score': 0.29,
    })

ingredient_x_product_datum.append({
    'ingredient': 'Carne Moída',
    'product': 'Carne Moído Congelado Friboi',
    'score': 0.29,
    })

ingredient_x_product_datum.append({
    'ingredient': 'Carne Moída',
    'product': 'Carne Moída Resfriada 1kg',
    'score': 0.79,
    })

ingredient_x_product_datum.append({
    'ingredient': 'Carne Moída',
    'product': 'Carne Moída Soja Superbom 250g',
    'score': 0.49,
    })

ingredient_x_product_datum.append({
    'ingredient': 'Molho de Tomate',
    'product': 'La Pianezza Molho de Tomate Tradicional',
    'score': 0.96,
    })

ingredient_x_product_datum.append({
    'ingredient': 'Molho de Tomate',
    'product': 'Molho de Tomate Tradicional Predilecta 340G',
    'score': 0.68,
    })

def replace_name_to_id(ingredient_x_product_data):
    ret = session.execute(
            sa.select(ingredient.c.id).
            where(
                ingredient.c.name ==
                    ingredient_x_product_data['ingredient']
                 )
            )
    [ingredient_id] = ret.fetchone()
    ingredient_x_product_data['ingredient_id'] = ingredient_id
    del ingredient_x_product_data['ingredient']
    ret = session.execute(
            sa.select(product.c.id).
            where(
                product.c.name ==
                    ingredient_x_product_data['product']
                 )
            )
    [product_id] = ret.fetchone()
    ingredient_x_product_data['product_id'] = product_id
    del ingredient_x_product_data['product']
    return ingredient_x_product_data

def upgrade():
    for ingredient_x_product_data in ingredient_x_product_datum:
        ingredient_x_product_data = deepcopy(ingredient_x_product_data)
        ingredient_x_product_data = replace_name_to_id(
                ingredient_x_product_data
                )
        session.execute(
                sa.insert(ingredient_x_product).
                values(ingredient_x_product_data)
                )


def downgrade():
    for ingredient_x_product_data in ingredient_x_product_datum:
        ingredient_x_product_data = deepcopy(ingredient_x_product_data)
        ingredient_x_product_data = replace_name_to_id(
                ingredient_x_product_data
                )
        session.execute(
                sa.delete(ingredient_x_product).
                where(
                    sa.sql.and_(
                        (ingredient_x_product.c.ingredient_id == 
                            ingredient_x_product_data['ingredient_id']),
                        (ingredient_x_product.c.product_id ==
                            ingredient_x_product_data['product_id'])
                        )
                    )
                )
