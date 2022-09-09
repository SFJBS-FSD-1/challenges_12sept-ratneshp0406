from flask import Flask, request, jsonify

app = Flask(__name__)

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
# /recipes   GET  to get all recipes

@app.route("/recipes/", methods=["GET"])
def recipes_get():
    if request.method == "GET":
        #data = user_list[0]
        json_data = jsonify(recipes)

        return json_data



# /recipes/<id> GET to get matching id

@app.route("/recipes/<int:id>", methods=["GET"])
def recipes_id_get(id):
    if request.method == "GET":
        for i in recipes:
            if i['id'] == id:
                data = jsonify(i)
                return data
        else:
            return ("id not matches")

@app.route("/recipes/<int:id>", methods=["DELETE"])
def recipes_delete(id):
    if request.method == "DELETE":
        for i in recipes:
            if i['id'] == id:
                i.clear()
        return recipes

@app.route("/recipes/<int:id>/", methods=["PUT"])
def recipes_put(id):
    if request.method == "PUT":
        for i in recipes:
            if i['id'] == id:
                data = request.get_json()
                i.update({"id": data["id"],'name': data["name"],"description": data["description"]})
                return jsonify(i)
        else:
            return ("give proper input")
            return jsonify({"mesage":"recepie not found"})



app.run()