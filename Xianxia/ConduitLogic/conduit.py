from Xianxia.ConduitLogic.iconduit import IConduit

class Conduit(IConduit):
    def __init__(self, name: str, damage_type: str):
        self._name = name
        self._damage_type = damage_type

    def get_damage_type(self) -> str:
        return self._damage_type

    def get_name(self) -> str:
        return self._name

    # Default behavior (can be overridden)
    def deal_damage(self, attacker, target) -> float:
        return attacker.attack

    def apply_effect(self, attacker, target):
        pass

    def break_shield(self, target):
        pass


