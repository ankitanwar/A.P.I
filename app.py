from flask import Flask
from flask_restful import Api,Resource
from os import environ
from db import db
import config
from resources.item import Item
from resources.user import User,UserLogin
from flask_jwt_extended import JWTManager

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['JWT_SECRET_KEY']="verysecret"

api=Api(app)
db.init_app(app)
jwt = JWTManager(app)

@app.before_first_request
def create_table():
    db.create_all()

class Home(Resource):
    def get(self):
        return {"Hello":"World"}

api.add_resource(Item,"/item/<string:name>")
api.add_resource(User,"/user/<string:name>")
api.add_resource(Home,"/")
api.add_resource(UserLogin,"/login")



if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)