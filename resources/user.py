from flask_restful import Resource
from flask import request
from models.user import UserModel
from schema.user import UserSchema
from flask_jwt_extended import create_access_token,create_refresh_token

user_schema=UserSchema()

class User(Resource):
    def get(self,name):
        find=UserModel.search_by_name(name)
        if find:
            return{"id":find.id,"name":find.name}
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

class UserLogin(Resource):
    
    def post(self):
        try:
            user_json = request.get_json()
            user_data = user_schema.load(user_json)

        except Exception as e:
            return {"message":"Some error has been occured {}".format(e)}

        user = UserModel.search_by_name(user_data['name'])
        
        if user and user_data['password']==user.password:
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}

        return {"message": "INVALID CREDENTIALS"}