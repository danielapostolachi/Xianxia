from Xianxia.CombatLogic.criticalsystem import CriticalSystem
from Xianxia.CombatLogic.damagesystem import DamageSystem
from Xianxia.CombatLogic.shieldsystem import ShieldSystem
from Xianxia.CombatLogic.turnmanager import TurnManager


class CombatFacade:
    def __init__(self):
        self.turn_manager = TurnManager()
        self.shield_system = ShieldSystem()
        self.crit_system = CriticalSystem()
        self.damage_system = DamageSystem()

    def start_battle(self, units):
        self.turn_manager.roll_initiative(units)

    def execute_action(self, attacker, ability, target):
        # 1. base damage from ability
        base_damage = ability.execute(attacker, target, self)

        # 2. crit check
        if self.crit_system.roll_crit(attacker):
            base_damage = self.crit_system.apply_crit(base_damage)
            attacker.conduit.apply_effect(attacker, target)

        # 3. final damage (true damage, etc.)
        final_damage = self.damage_system.calculate_final_damage(
            attacker, target, base_damage
        )

        # 4. apply to shields / HP
        self.shield_system.apply_damage(target, final_damage, attacker.conduit.get_damage_type())

        # 5. next turn
        self.turn_manager.next_turn()