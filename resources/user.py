from flask_restful import Resource
from flask import request
from models.user import UserModel
from schema.user import UserSchema

user_schema=UserSchema()

class User(Resource):
    def get(self,name):
        find=UserModel.search_by_name(name)
        if find:
            print("the value of find is ",find[0].name)
        else:
            return {"message":"User doesnt exist in the databse"}
    
    def post(self,name):
        data_json=request.get_json()
        data_json['name']=name

        data=user_schema.load(data_json)

        try:
            user=UserModel(**data)
            user.save_to_db()
            return {"message":"user has been added to the database Sucessfully"}
        
        except Exception as e:
            return {"message":"Some error has been occured{}".format(e)}

