from flask_restful import Resource,reqparse
from models.item import ItemModel

class Item(Resource):

    sender=reqparse.RequestParser()
    sender.add_argument('price',required=True,type=int,help='Price field cannot be empty')

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
            incoming_data=Item.sender.parse_args()
            data=ItemModel(name,incoming_data['price'])
            try:
                data.save_to_db()
                return {"Message":"Item has been added to the database Successfully"}
            except Exception as e:
                return {"Message":"Some error has been occured {}".format(e)}

    
