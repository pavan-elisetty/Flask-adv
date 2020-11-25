from ma import ma
from models.item import ItemModel
from models.store import StoreModel

class ItemSchema(ma.ModelSchema): #since it is already linked
    class Meta: #since password is returning , creating this will make password only to load not to return
        model=ItemModel
        load_only=("store",) #tuple is required
        dump_only=("id",) #since its not bing loaded
        include_fk=True