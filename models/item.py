from db import db

class ItemModel(db.Model):

    __tablename__='items'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),unique=True,nullable=False)
    price=db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("UserModel")

    @classmethod
    def search_by_name(cls,name):
        search = db.session.query(ItemModel).filter(ItemModel.name == name).first()
        if search:
            return search

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_frm_db(self):
        db.session.delete(self)
        db.session.commit()


    