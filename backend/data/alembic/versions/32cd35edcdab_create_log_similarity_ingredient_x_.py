"""create log_similarity_ingredient_x_product_customer

Revision ID: 32cd35edcdab
Revises: 9081c198b091
Create Date: 2022-02-20 05:05:05.016032

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from copy import deepcopy


# revision identifiers, used by Alembic.
revision = '32cd35edcdab'
down_revision = '9081c198b091'
branch_labels = None
depends_on = '9081c198b091'

try:
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    metadata = sa.schema.MetaData(bind=bind)
    customer = sa.Table(
            'customer',
            metadata,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(200), nullable=False),
            )

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

    log_ingredient_x_product = sa.Table(
            'log_similarity_ingredient_x_product_customer',
            metadata,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('customer_id', sa.Integer, sa.ForeignKey('customer.id'), nullable=False),
            sa.Column('ingredient_id', sa.Integer, sa.ForeignKey('ingredient.id'), nullable=False),
            sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id'), nullable=False),
            )
except NameError:
    pass

customer_datum = []
customer_datum.append({
    'name': 'Customer',
    'log_ingredient_x_product': [
        {
            'ingredient': 'Massa de Lasanha',
            'product': 'Massa Para Lasanha Renata'
        },
        {
            'ingredient': 'Massa de Lasanha',
            'product': 'Massa Para Lasanha Renata'
        },
        {
            'ingredient': 'Massa de Lasanha',
            'product': 'Massa Para Lasanha Renata'
        },
        {
            'ingredient': 'Massa de Lasanha',
            'product': 'Massa Fresca Para Lasanha Caue'
        },
        {
            'ingredient': 'Massa de Lasanha',
            'product': 'Massa Fresca Para Lasanha Caue'
        },
        {
            'ingredient': 'Massa de Lasanha',
            'product': 'Massa Fresca Para Lasanha Caue'
        },
        {
            'ingredient': 'Massa de Lasanha',
            'product': 'Massa Fresca Para Lasanha Caue'
        },
        {
            'ingredient': 'Massa de Lasanha',
            'product': 'Massa Fresca Para Lasanha Caue'
        },
        {
            'ingredient': 'Massa de Lasanha',
            'product': 'Massa Fresca Para Lasanha Caue'
        },
        {
            'ingredient': 'Massa de Lasanha',
            'product': 'Massa Fresca Para Lasanha Caue'
        },
        ]
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
    def upgrade_log(log_ingredient_x_product_datum, customer_id):
        for log_ingredient_x_product_data in log_ingredient_x_product_datum:
            log_ingredient_x_product_data = deepcopy(log_ingredient_x_product_data)
            log_ingredient_x_product_data['customer_id'] = customer_id
            log_ingredient_x_product_data = replace_name_to_id(
                    log_ingredient_x_product_data
                    )
            session.execute(
                    sa.insert(log_ingredient_x_product).
                    values(log_ingredient_x_product_data)
                    )

    for customer_data in customer_datum:
        customer_data = deepcopy(customer_data)
        log_ingredient_x_product_datum = []
        if 'log_ingredient_x_product' in customer_data:
            log_ingredient_x_product_datum = customer_data['log_ingredient_x_product']
            del customer_data['log_ingredient_x_product']
        ret = session.execute(
                sa.insert(customer).
                values(customer_data).
                returning(customer.c.id)
                )
        [customer_id] = ret.fetchone()
        upgrade_log(log_ingredient_x_product_datum, customer_id)




def downgrade():
    # TODO
    pass
