#turning to marshmallow as reqparse maybe susupended

from ma import ma
from models.user import UserModel


class UserSchema(ma.ModelSchema): #since it is already linked
    class Meta: #since password is returning , creating this will make password only to load not to return
        model=UserModel
        load_only=("password",) #tuple is required
        dump_only=("id",) #since its not bing loaded
