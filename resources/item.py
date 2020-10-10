from flask_restful import Resource,reqparse
from flask import request
from models.item import ItemModel
from schema.items import ItemSchema

item_schema=ItemSchema()

class Item(Resource):

    def get(self,name):
        find=ItemModel.search_by_name(name)
        if find:
            return {"name":find.name,"price":find.price}
        else:
            return {"message":"Item doesn't exist in the database"}

    def post(self,name):
        find=ItemModel.search_by_name(name)
        if find:
            return {"message":"Item with name {} already exist in the database".format(name)}
        else:
            json_data=request.get_json()
            json_data['name']=name

            data=item_schema.load(json_data)
            
            data=ItemModel(**data)
            try:
                data.save_to_db()
                return {"Message":"Item has been added to the database Successfully"}
            except Exception as e:
                return {"Message":"Some error has been occured {}".format(e)}

    
