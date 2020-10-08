from flask import Flask
from flask_restful import Api,Resource
from db import db
import config
from resources.item import Item

app=Flask(__name__)
app.config.from_envvar('APP_SETTINGS')


api=Api(app)
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()

class Home(Resource):
    def get(self):
        return {"Hello":"World"}

api.add_resource(Item,"/<string:name>")
api.add_resource(Home,"/")



if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)