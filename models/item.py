from db import db

class ItemModel(db.Model):

    __tablename__='itemss'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),unique=True)
    price=db.Column(db.Integer)


    def __init__(self,name,price):
        self.name=name
        self.price=price

    @classmethod
    def search_by_name(cls,name):
        search = db.session.query(ItemModel).filter(ItemModel.name == name).first()
        if search:
            return search

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    