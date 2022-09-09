from flask import Flask, jsonify, request

from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

recipes = [
    {
        'id': 1,
        'name': 'Salad',
        'description': 'This is a lovely Greek salad recipe.'
    },
    {
        'id': 2,
        'name': 'Rava Masala Dosa',
        'description': 'This is recipe for Rava Masala Dosa.'
    }
]

class allRecipes(Resource):
    def get(self):
        return jsonify(recipes)

    def post(self):
        data = request.get_json()
        recipes.append(data)
        return jsonify(recipes)


class oneRecipe(Resource):
    def get(self, recipe_id):
        for recipe in recipes:
            if recipe["id"] == recipe_id:
                return jsonify(recipe)
        else:
            return jsonify({"message": "Id not found"})

    def put(self, recipe_id):
        for i in recipes:
            if i["id"] == recipe_id:
                data = request.get_json()
                i.update({"id":data["id"], "name":data["name"], "description": data["description"]})
                return jsonify(recipes)
            else:
                return jsonify({"message":"not found"})

    def delete(self, recipe_id):
        for i in recipes:
            if i["id"] == recipe_id:
                recipes.remove(i)
                return jsonify(recipes)
        else:
            return jsonify({"message": "not found"})

api.add_resource(allRecipes, "/recipes")
api.add_resource(oneRecipe,"/recipes/<int:recipe_id>")

app.run()