import sqlalchemy as sa
import os
import pandas as pd
import sklearn

# ainda não temos variáveis suficiente para um modelo
# mais complexo de inteligência artificial
# por isso esse script de treinamento usará
# apenas uma conta proporcional
#
# a medida que formos implementando mais funcionalidades
# vamos utilizar um modelo mais complexo

engine = sa.create_engine(os.environ['SQLALCHEMY_URL'])

metadata = sa.MetaData()
ai = sa.Table(
        'ai_similarity_ingredient_x_product_customer',
        metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('customer_id', sa.Integer, sa.ForeignKey('customer.id'), nullable=False),
        sa.Column('ingredient_id', sa.Integer, sa.ForeignKey('ingredient.id'), nullable=False),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id'), nullable=False),
        sa.Column('score', sa.Float, nullable=False),
        )

sql = '''
SELECT DISTINCT
    customer_id,
    ingredient_id,
    product_id,
    CAST(quant AS float)/CAST(total AS float) score
FROM (
        SELECT
            l.customer_id,
            l.ingredient_id,
            l.product_id,
            COUNT(1) OVER (PARTITION BY l.customer_id, l.ingredient_id, l.product_id) quant,
            COUNT(1) OVER (PARTITION BY l.customer_id, l.ingredient_id) total 
        FROM
            log_similarity_ingredient_x_product_customer l
      ) subquery;
'''

df = pd.read_sql_query(sql, con=engine)

for index, row in df.iterrows():
    with engine.connect() as connection:
        try:
            connection.execute(
                    sa.insert(ai).
                    values(row)
                    )
        except sa.exc.IntegrityError:
            connection.execute(
                    sa.update(ai).
                    values({'score': row['score']}).
                    where(sa.sql.and_(
                        ai.c.customer_id == int(row['customer_id']),
                        ai.c.ingredient_id == int(row['ingredient_id']),
                        ai.c.product_id == int(row['product_id'])
                        )
                        )
                    )
            print(str(
                    sa.update(ai).
                    values({'score': row['score']}).
                    where(sa.sql.and_(
                        ai.c.customer_id == int(row['customer_id']),
                        ai.c.ingredient_id == int(row['ingredient_id']),
                        ai.c.product_id == int(row['product_id'])
                        )
                        )
                    ))

