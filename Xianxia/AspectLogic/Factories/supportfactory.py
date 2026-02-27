from Xianxia.AspectLogic.aspectfactory import AspectFactory
from Xianxia.AspectLogic.Products.supportaspects import Fortune, Emotions, Unity

class SupportFactory(AspectFactory):

    def create_aspect(self, subrole: str):
        if subrole == "fortune":
            return Fortune()
        elif subrole == "emotions":
            return Emotions()
        elif subrole == "unity":
            return Unity()
        else:
            raise ValueError("Invalid Support subrole")