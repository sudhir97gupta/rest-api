from flask import Flask, request
from resources.item import blp as ItemBluePrint
from flask_smorest import Api

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Items Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)

api.register_blueprint(ItemBluePrint)




###################################
# from flask import Flask, request, jsonify, render_template

# app = Flask(__name__)

# items = [
#     {"Item-Name": "Paneer Masala", "Price": 220},
#     {"Item-Name": "Paneer Tikka", "Price": 260}
# ]

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.get("/get_items")
# def get_items():
#     return jsonify(items)

# @app.post("/add_item")
# def add_item():
#     request_data = request.get_json()
#     for item in items:
#         if request_data['Item-Name'] == item['Item-Name']:
#             return jsonify({'message': "Item already present"}), 201
#     items.append(request_data)
#     return jsonify({'message': "Item added successfully"}), 201

# @app.get("/get_item")
# def get_item():
#     name = request.args.get('Item-Name')
#     for item in items:
#         if name == item['Item-Name']:
#             return jsonify(item)
#     return jsonify({'message': "Item doesn't exist"}), 404

# @app.put("/update_item")
# def update_item():
#     request_data = request.get_json()
#     for item in items:
#         if request_data['Item-Name'] == item['Item-Name']:
#             item['Price'] = request_data['Price']
#             return jsonify({'message': "Item updated successfully"}), 200
#     return jsonify({'message': "Item doesn't exist"}), 404

# if __name__ == "__main__":
#     app.run(debug=True)
