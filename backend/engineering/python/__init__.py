import os
import json
from copy import deepcopy

from flask import Flask, request, jsonify
import sqlalchemy as sa
from backend.engineering.python import model


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/recipe/<string:recipe_name>/ingredients')
    def ingredients(recipe_name):
        engine = sa.create_engine(os.environ['SQLALCHEMY_URL'])
        ingredient_datum = model.get_ingredients_by_recipe_name(
                engine, recipe_name
                )
        return jsonify(ingredient_datum)

    @app.route('/recipe/<string:recipe_name>/product_recomendation')
    def product_recomendation(recipe_name):
        restrictions = request.args.get('restrictions')
        engine = sa.create_engine(os.environ['SQLALCHEMY_URL'])
        ingredient_datum = model.get_ingredients_by_recipe_name(
                engine, recipe_name
                )
        result = []
        for ingredient_data in ingredient_datum:
            result_ingredient = deepcopy(ingredient_data)
            result_ingredient['product_recomendation'] = (
                    model.get_product_recomendation_by_ingredient_id(
                        engine, ingredient_data['id']
                        )
                    )
            result.append(result_ingredient)
        return jsonify(result)

    return app
