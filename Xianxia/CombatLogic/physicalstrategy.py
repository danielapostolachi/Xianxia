from Xianxia.CombatLogic.damagestrategy import DamageStrategy


class PhysicalStrategy(DamageStrategy):
    def calculate(self, attacker, target):
        return attacker.attack * 1.0