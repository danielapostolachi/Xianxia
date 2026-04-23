from Xianxia.CombatLogic.damageimplementor import DamageImplementor


class PhysicalDamage(DamageImplementor):
    def calculate(self, attacker, target):
        return attacker.attack * 1.0