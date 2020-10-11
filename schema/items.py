from ma import ma 
from models.item import ItemModel
from models.user import UserModel

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=ItemModel
        include_fk=True

