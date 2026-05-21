from Xianxia.Mess.AspectLogic.aspectfactory import AspectFactory
from Xianxia.Mess.AspectLogic.Products.utilityaspect import Beginnings, Creativity, Balance

class UtilityFactory(AspectFactory):

    def create_aspect(self, subrole: str):
        if subrole == "beginnings":
            return Beginnings()
        elif subrole == "creativity":
            return Creativity()
        elif subrole == "balance":
            return Balance()
        else:
            raise ValueError("Invalid Sustain subrole")