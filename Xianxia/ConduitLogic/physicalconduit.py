from Xianxia.ConduitLogic.conduit import Conduit


class PhysicalConduit(Conduit):
    def __init__(self, name: str):
        super().__init__(name, "Physical")

    def deal_damage(self, attacker, target) -> float:
        return attacker.attack * 1.0

    def apply_effect(self, attacker, target):
        if attacker.crit:  # assuming you have crit logic
            target.apply_status("wound", duration=2)

    def break_shield(self, target):
        target.sorcery_shield -= 1