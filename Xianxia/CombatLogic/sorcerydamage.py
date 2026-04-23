from Xianxia.CombatLogic.damageimplementor import DamageImplementor


class SorceryDamage(DamageImplementor):
    def calculate(self, attacker, target):
        return attacker.attack * 1.2