from db import db

class UserModel(db.Model):

    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(20))


    def __init__(self,name,password):
        self.name=name
        self.password=password
    
    @classmethod
    def search_by_name(cls,name):
        search = db.session.query(UserModel).filter(UserModel.name == name).first()
        if search:
            return search

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    