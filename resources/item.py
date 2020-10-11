from flask_restful import Resource,reqparse
from flask import request
from models.item import ItemModel
from schema.items import ItemSchema
from flask_jwt_extended import jwt_required,fresh_jwt_required
from models.user import UserModel

item_schema=ItemSchema()

class Item(Resource):

    def get(self,name):
        find=ItemModel.search_by_name(name)
        if find:
            return {"name":find.name,"price":find.price}
        else:
            return {"message":"Item doesn't exist in the database"}

    @fresh_jwt_required
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

    @jwt_required
    def delete(self,name):
        data=request.get_json()
        user=UserModel.search_by_name(data['name'])

        if user:
            _id=user.id
            find=ItemModel.search_by_name(name)
            if find and _id==find.user_id:
                try:
                    find.delete_frm_db()
                    return {"message":"item has been deleted from the database"}
                except Exception as e:
                    return {"message":"Some error has been occured {}".format(e)}
            else:
                return {"message":"User id doen't match"}
        else:
            return {"message":"Invalid id and password "}                        


    
