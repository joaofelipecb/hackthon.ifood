"""grocery_data

Revision ID: 3b66497958b1
Revises: 89a32d285457
Create Date: 2022-02-19 21:28:44.248962

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from copy import deepcopy


# revision identifiers, used by Alembic.
revision = '3b66497958b1'
down_revision = '89a32d285457'
branch_labels = None
depends_on = '89a32d285457'

try:
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    metadata = sa.schema.MetaData(bind=bind)
    grocery = sa.Table(
        'grocery',
        metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('shipping_cost', sa.Float, nullable=False),
        sa.Column('shipping_cost_distance_unit', sa.String(20), nullable=False),
        sa.Column('shipping_cost_currency_unit', sa.String(20), nullable=False),
        sa.Column('geolocalization_latitude', sa.Float, nullable=False),
        sa.Column('geolocalization_longitude', sa.Float, nullable=False),
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

    product_x_grocery = sa.Table(
        'product_x_grocery',
        metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('grocery_id', sa.Integer, sa.ForeignKey('grocery.id'), nullable=False),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id'), nullable=False),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('price_currency_unit', sa.String(20), nullable=False),
        )
except NameError:
    pass

grocery_datum = []
grocery_datum.append({
    'name': 'Mercado 1',
    'shipping_cost': 0.50,
    'shipping_cost_distance_unit': 'km',
    'shipping_cost_currency_unit': 'R$',
    'geolocalization_latitude': -24.2162481,
    'geolocalization_longitude': -48.4374516,
    'product':[
        {
            'name': 'Massa Para Lasanha Renata',
            'image': 'https://trimais.vteximg.com.br/arquivos/ids/1008133-1000-1000/foto_original.jpg?v=637395834287270000',
            'amount': 200,
            'amount_unit': 'g',
            'price': 10.60,
            'price_currency_unit': 'R$',
            'vegetarian': True,
            'vegan': True,
            'diet': False,
            'light': False,
            'lactose_free': False,
            'gluten_free': False,
        },
        {
            'name': 'Massa Fresca Para Lasanha Caue',
            'image': 'https://static.distribuidoracaue.com.br/media/catalog/product/cache/1/thumbnail/9df78eab33525d08d6e5fb8d27136e95/m/a/massa_lasanha_massa_leve.jpg?v=1',
            'amount': 500,
            'amount_unit': 'g',
            'price': 15.20,
            'price_currency_unit': 'R$',
            'vegetarian': True,
            'vegan': True,
            'diet': False,
            'light': False,
            'lactose_free': False,
            'gluten_free': False,
        },
        {
            'name': 'Lasanha Massa Vitarella',
            'image': 'https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcT4MeDYG4agyas1jiyBR20hxwOU58PS5zauAyKvLnHK7PvGmL0EeUUAFFZL8KxP8fBcDJUpzsIf5Z7yhHdOUua_F0GFWYou2kfYj54y3DI&usqp=CAE',
            'amount': 500,
            'amount_unit': 'g',
            'price': 9.20,
            'price_currency_unit': 'R$',
            'vegetarian': True,
            'vegan': True,
            'diet': False,
            'light': False,
            'lactose_free': False,
            'gluten_free': False,
        },
        {
            'name': 'Massa para Lasanha e Canelone DA BOA',
            'image': 'https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQtaI0R4Db1JDIj_pl9CE1iuvlEKp8eSTgM54OA6ldQVCy6NeA7jblnF8givCywPnVzIGl4xKvRR2CZHHCs8RS2l2JqQGOf&usqp=CAE',
            'amount': 500,
            'amount_unit': 'g',
            'price': 5.20,
            'price_currency_unit': 'R$',
            'vegetarian': True,
            'vegan': True,
            'diet': False,
            'light': False,
            'lactose_free': False,
            'gluten_free': False,
        },
        {
            'name': 'Carne Moído Congelado Friboi',
            'image': 'https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcSDcqjA5sEeM8sjvnlbyaXtnTnOrKDToZfoVYW7lsHVKjAyt9AzIC_0jTRU0Ds66bqTZiMT6N68bz2ysHIUjsZFyIniLvERqO6gMc7et0ZI7eMdo-t7wDTx&usqp=CAE',
            'amount': 500,
            'amount_unit': 'g',
            'price': 14.99,
            'price_currency_unit': 'R$',
            'vegetarian': False,
            'vegan': False,
            'diet': False,
            'light': False,
            'lactose_free': False,
            'gluten_free': False,
        },
        {
            'name': 'Carne Moída Resfriada 1kg',
            'image': 'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcTai1NMSinyKjHQIUQMQLWhUS4yX7c9Fao44hZFjQX8x2qsExeIAenm_CR7_WC7Priz2Y_RsetcHIRv79GqsHmtg8PzKaSJ&usqp=CAE',
            'amount': 1000,
            'amount_unit': 'g',
            'price': 24.00,
            'price_currency_unit': 'R$',
            'vegetarian': False,
            'vegan': False,
            'diet': False,
            'light': False,
            'lactose_free': False,
            'gluten_free': False,
        },
        {
            'name': 'Carne Moída Soja Superbom 250g',
            'image': 'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQWZs8mMuoE_6cnYCxsal6EFDWm4lnhMI5fZReFsIGGWuNtfmxN4QtR4ZdXZpqAvJjkyEagtHdF8uuU7JK-AxbWhMOKlSdj9WoDGVuIOf2pH0ZpxlhQ3Y17Ng&usqp=CAE',
            'amount': 250,
            'amount_unit': 'g',
            'price': 23.99,
            'price_currency_unit': 'R$',
            'vegetarian': True,
            'vegan': True,
            'diet': False,
            'light': False,
            'lactose_free': False,
            'gluten_free': False,
        },
        {
            'name': 'La Pianezza Molho de Tomate Tradicional',
            'image': 'https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcTqeo66z8SBYcLr4T3HN-alSorL6cdZhMjkPi3aGurD-PnAezTI9wrZfc94Nf18uZPbGi-E7cRlD-r0olUZMVOrDK1kxWOYe-I3dnu6ekaYQAauFwvECA-3&usqp=CAE',
            'amount': 300,
            'amount_unit': 'g',
            'price': 8.10,
            'price_currency_unit': 'R$',
            'vegetarian': True,
            'vegan': True,
            'diet': False,
            'light': False,
            'lactose_free': False,
            'gluten_free': False,
        },
        {
            'name': 'Molho de Tomate Tradicional Predilecta 340G',
            'image': 'https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSPmPD5jEf57cPomgZ9nvihJAURxxRIXA5VkcX3lWHbfhUJJSFfNn2rWrYanFXYRJKoMKNcrBWmVXsXdkoHSJWont-6rdTZqf0PV-tNml4d&usqp=CAE',
            'amount': 340,
            'amount_unit': 'g',
            'price': 1.10,
            'price_currency_unit': 'R$',
            'vegetarian': True,
            'vegan': True,
            'diet': False,
            'light': False,
            'lactose_free': False,
            'gluten_free': False,
        },
        ]
    })

def split_product_normalized(product_x_grocery_data):
    product_data = {
            'name': product_x_grocery_data['name'],
            'image': product_x_grocery_data['image'],
            'amount': product_x_grocery_data['amount'],
            'amount_unit': product_x_grocery_data['amount_unit'],
            'vegetarian': product_x_grocery_data['vegetarian'],
            'vegan': product_x_grocery_data['vegan'],
            'diet': product_x_grocery_data['diet'],
            'light': product_x_grocery_data['light'],
            'lactose_free': product_x_grocery_data['lactose_free'],
            'gluten_free': product_x_grocery_data['gluten_free'],
            }
    del product_x_grocery_data['name']
    del product_x_grocery_data['image']
    del product_x_grocery_data['amount']
    del product_x_grocery_data['amount_unit']
    del product_x_grocery_data['vegetarian']
    del product_x_grocery_data['vegan']
    del product_x_grocery_data['diet']
    del product_x_grocery_data['light']
    del product_x_grocery_data['lactose_free']
    del product_x_grocery_data['gluten_free']
    return product_data, product_x_grocery_data


def upgrade():
    def upgrade_product(product_x_grocery_datum, grocery_id):
        for product_x_grocery_data in product_x_grocery_datum:
            product_x_grocery_data = deepcopy(product_x_grocery_data)
            product_x_grocery_data['grocery_id'] = grocery_id
            product_data, product_x_grocery_data = (
                    split_product_normalized(product_x_grocery_data)
                    )
            try:
                ret = session.execute(
                        sa.insert(product).
                        values(product_data).
                        returning(product.c.id)
                        )
                [product_id] = ret.fetchone()
            except sa.exc.IntegrityError:
                ret = session.execute(
                        sa.select(product).
                        where(product.c.name == product_data['name'])
                        )
                [product_id] = ret.fetchone()
            product_x_grocery_data['product_id'] = product_id
            ret = session.execute(
                    sa.insert(product_x_grocery).
                    values(product_x_grocery_data)
                    )

    for grocery_data in grocery_datum:
        grocery_data = deepcopy(grocery_data)
        product_x_grocery_datum = []
        if 'product' in grocery_data:
            product_x_grocery_datum = deepcopy(grocery_data['product'])
            del grocery_data['product']
        ret = session.execute(
                sa.insert(grocery).values(grocery_data).
                returning(grocery.c.id)
                )
        [grocery_id] = ret.fetchone()
        upgrade_product(product_x_grocery_datum, grocery_id)


def downgrade():
    def downgrade_product(product_x_grocery_datum, grocery_id):
        for product_x_grocery_data in product_x_grocery_datum:
            product_x_grocery_data = deepcopy(product_x_grocery_data)
            product_x_grocery_data['grocery_id'] = grocery_id
            product_data, product_x_grocery_data = (
                    split_product_normalized(product_x_grocery_data)
                    )
            ret = session.execute(
                    sa.select(product.c.id).
                    where(product.c.name == product_data['name'])
                    )
            [product_id] = ret.fetchone()
            product_x_grocery_data['ingredient_id'] = product_id
            op.execute(
                    product_x_grocery.delete().
                    where(
                        product_x_grocery.c.grocery_id
                            == product_x_grocery_data['grocery_id']
                        and product_x_grocery.c.product_id
                            == product_x_grocery_data['product_id']
                        )
                    )
            try:
                op.execute(
                        product.delete().
                        where(
                            product.c.id == product_id
                            )
                        )
            except sa.exc.IntegrityError:
                pass

    for grocery_data in grocery_datum:
        grocery_data = deepcopy(grocery_data)
        product_x_grocery_datum = []
        if 'product' in grocery_data:
            product_x_grocery_datum = deepcopy(grocery_data['product'])
            del grocery_data['product']
        ret = session.execute(
                sa.select(grocery.c.id).
                where(grocery.c.name == grocery_data['name'])
                )
        [grocery_id] = ret.fetchone()
        downgrade_product(product_x_grocery_datum, grocery_id)
        op.execute(
                grocery.delete().
                where(grocery.c.name == grocery_data['name'])
                )

