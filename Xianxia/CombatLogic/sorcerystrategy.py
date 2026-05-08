from Xianxia.CombatLogic.damagestrategy import DamageStrategy


class SorceryStrategy(DamageStrategy):
    def calculate(self, attacker, target):
        return attacker.attack * 1.2