from Xianxia.ConduitLogic.iconduit import IConduit

class Conduit(IConduit):
    def __init__(self, name: str, damage_type: str):
        self._name = name
        self._damage_type = damage_type

    def get_damage_type(self) -> str:
        return self._damage_type

    def get_name(self) -> str:
        return self._name

class PhysicalConduit(Conduit):
    def __init__(self, name: str):
        super().__init__(name, "Physical")

class SorceryConduit(Conduit):
    def __init__(self, name: str):
        super().__init__(name, "Sorcery")

class FusionConduit(Conduit):
    def __init__(self, name: str):
        super().__init__(name, "Fusion")


