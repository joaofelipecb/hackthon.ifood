"""empty message

Revision ID: 157e941a0231
Revises: 
Create Date: 2022-02-19 15:41:11.939173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '157e941a0231'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            'recipe',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(200), nullable=False),
            sa.Column('description', sa.Unicode(500)),
            )

    op.create_table(
            'ingredient',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(200), nullable=False),
            )
    op.create_unique_constraint('uq_ingredient_name', 'ingredient', ['name'])

    op.create_table(
            'ingredient_x_recipe',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('recipe_id', sa.Integer, sa.ForeignKey('recipe.id'), nullable=False),
            sa.Column('ingredient_id', sa.Integer, sa.ForeignKey('ingredient.id'), nullable=False),
            sa.Column('amount', sa.Float, nullable=False),
            sa.Column('amount_unit', sa.String(20), nullable=False),
            )

    op.create_table(
            'grocery',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(200), nullable=False),
            sa.Column('shipping_cost', sa.Float, nullable=False),
            sa.Column('shipping_cost_distance_unit', sa.String(20), nullable=False),
            sa.Column('shipping_cost_currency_unit', sa.String(20), nullable=False),
            sa.Column('geolocalization_latitude', sa.Float, nullable=False),
            sa.Column('geolocalization_longitude', sa.Float, nullable=False),
            )

    op.create_table(
            'product',
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
    op.create_unique_constraint('uq_product_name', 'product', ['name'])

    op.create_table(
            'product_x_grocery',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('grocery_id', sa.Integer, sa.ForeignKey('grocery.id'), nullable=False),
            sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id'), nullable=False),
            sa.Column('price', sa.Float, nullable=False),
            sa.Column('price_currency_unit', sa.String(20), nullable=False),
            )

    op.create_table(
            'customer',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(200), nullable=False),
            )

    op.create_table(
            'ai_weight_customer',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('customer_id', sa.Integer, sa.ForeignKey('customer.id'), nullable=False),
            sa.Column('lowest_total_price', sa.Float, nullable=False),
            sa.Column('best_cost_benefit', sa.Float, nullable=False),
            sa.Column('lowest_time_to_ship', sa.Float, nullable=False),
            )

    op.create_table(
            'ai_weight_default',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('lowest_total_price', sa.Float, nullable=False),
            sa.Column('best_cost_benefit', sa.Float, nullable=False),
            sa.Column('lowest_time_to_ship', sa.Float, nullable=False),
            )

    op.create_table(
            'ai_similarity_ingredient_x_product_customer',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('customer_id', sa.Integer, sa.ForeignKey('customer.id'), nullable=False),
            sa.Column('ingredient_id', sa.Integer, sa.ForeignKey('ingredient.id'), nullable=False),
            sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id'), nullable=False),
            sa.Column('score', sa.Float, nullable=False),
            )

    op.create_table(
            'ai_similarity_ingredient_x_product_default',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('ingredient_id', sa.Integer, sa.ForeignKey('ingredient.id'), nullable=False),
            sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id'), nullable=False),
            sa.Column('score', sa.Float, nullable=False),
            )

    op.create_table(
            'log_similarity_ingredient_x_product_customer',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('customer_id', sa.Integer, sa.ForeignKey('customer.id'), nullable=False),
            sa.Column('ingredient_id', sa.Integer, sa.ForeignKey('ingredient.id'), nullable=False),
            sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id'), nullable=False),
            )


def downgrade():
    op.drop_table('log_similarity_ingredient_x_product_customer')
    op.drop_table('ai_similarity_ingredient_x_product_default')
    op.drop_table('ai_similarity_ingredient_x_product_customer')
    op.drop_table('ai_weight_default')
    op.drop_table('ai_weight_customer')
    op.drop_table('customer')
    op.drop_table('product_x_grocery')
    op.drop_constraint('uq_product_name', 'product')
    op.drop_table('product')
    op.drop_table('grocery')
    op.drop_table('ingredient_x_recipe')
    op.drop_constraint('uq_ingredient_name', 'ingredient')
    op.drop_table('ingredient')
    op.drop_table('recipe')

