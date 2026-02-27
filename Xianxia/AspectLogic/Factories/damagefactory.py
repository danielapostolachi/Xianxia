from Xianxia.AspectLogic.aspectfactory import AspectFactory
from Xianxia.AspectLogic.Products.damageaspects import Communication, Knowledge, Future

class DamageFactory(AspectFactory):

    def create_aspect(self, subrole: str):
        if subrole == "communication":
            return Communication()
        elif subrole == "knowledge":
            return Knowledge()
        elif subrole == "future":
            return Future()
        else:
            raise ValueError("Invalid Sustain subrole")