#from pydoc import describe
from flask import Flask, request
import uuid
from database import items
from flask.views import MethodView
from flask_smorest import Blueprint
from schema import ItemSchema

blp = Blueprint("items", __name__, description="Operation on items")

@blp.route("/item")

class Item(MethodView):
    def get(self):
        id = request.args.get('id')
        try:
            if(id == None):
              return items
            else:
              return items[id]
        except KeyError:
            return{'message' : "item doesn't exist"} 
        
    @blp.arguments(ItemSchema)
    def put(self, request_data):
        #request_data = request.get_json()
        id = request.args.get('id')
        if id in items.keys():
           items[id] = request_data
           return{'message' : "Item updated successfully"}           
        return{'message' : "Item doesn't exist"}
    
    @blp.arguments(ItemSchema)
    def post(self, request_data):
        #request_data = request.get_json()

        items[uuid.uuid4().hex] = request_data
        #items.append(request_data)
        return{'message' : "item added successfully"}, 201

