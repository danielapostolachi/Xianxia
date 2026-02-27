from Xianxia.AspectLogic.aspect import Aspect

class Communication(Aspect):
    def __init__(self):
        super().__init__("Damage", "Communication")

class Knowledge(Aspect):
    def __init__(self):
        super().__init__("Damage", "Knowledge")

class Future(Aspect):
    def __init__(self):
        super().__init__("Damage", "Future")