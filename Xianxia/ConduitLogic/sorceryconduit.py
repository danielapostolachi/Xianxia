from Xianxia.ConduitLogic.conduit import Conduit


class SorceryConduit(Conduit):
    def __init__(self, name: str):
        super().__init__(name, "Sorcery")

    def deal_damage(self, attacker, target) -> float:
        return attacker.attack * 1.2

    def apply_effect(self, attacker, target):
        if attacker.crit:
            target.apply_status("stun", duration=1)

    def break_shield(self, target):
        target.physical_shield -= 1