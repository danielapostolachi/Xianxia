from Xianxia.AspectLogic.aspect import Aspect

class Health(Aspect):
    def __init__(self):
        super().__init__("Sustain", "Health")

class Endings(Aspect):
    def __init__(self):
        super().__init__("Sustain", "Endings")

class Status(Aspect):
    def __init__(self):
        super().__init__("Sustain", "Status")