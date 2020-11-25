from ma import ma
from models.item import ItemModel
from models.store import StoreModel
from schemas.item import ItemSchema



class StoreSchema(ma.ModelSchema): #since it is already linked
    items = ma.Nested(ItemSchema, many=True)

    class Meta: #since password is returning , creating this will make password only to load not to return

        model=StoreModel
        dump_only=("id",) #since its not bing loaded
        include_fk=True