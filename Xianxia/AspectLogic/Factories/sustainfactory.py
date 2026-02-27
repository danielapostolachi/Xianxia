from Xianxia.AspectLogic.aspectfactory import AspectFactory
from Xianxia.AspectLogic.Products.sustainaspects import Health, Endings, Status

class SustainFactory(AspectFactory):

    def create_aspect(self, subrole: str):
        if subrole == "health":
            return Health()
        elif subrole == "endings":
            return Endings()
        elif subrole == "status":
            return Status()
        else:
            raise ValueError("Invalid Sustain subrole")