# CombatEntities/minion.py
from Xianxia.CombatEntities.combat_entity import CombatEntity
import random

class Minion(CombatEntity):
    def __init__(self, name, hp, conduit, speed=8, parent_boss=None):
        super().__init__(name, hp, conduit, speed)
        self._parent_boss = parent_boss
        self._phase_abilities = {1: []}

    def set_phase_abilities(self, phase, abilities):
        self._phase_abilities[phase] = abilities

    def notify_parent(self):
        if self._parent_boss:
            self._parent_boss.notify_minion_death(self)

    def check_ult_ready(self):
        return self._ult_ready

    def act(self, battle_session):
        abilities = self._phase_abilities.get(1, [])
        if abilities:
            ability = random.choice(abilities)
            targets = battle_session.get_player_party().alive_members()
            ability.execute(self, targets, battle_session)

    def take_damage(self, damage, damage_conduit, is_true_damage=False):
        super().take_damage(damage, damage_conduit, is_true_damage)
        if not self.is_alive():
            self.notify_parent()