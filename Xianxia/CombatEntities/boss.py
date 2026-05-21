# boss.py
from Xianxia.CombatEntities.combat_entity import CombatEntity
import random

class Boss(CombatEntity):
    def __init__(self, name, hp, conduit, speed=10, max_phases=3):
        super().__init__(name, hp, conduit, speed)
        self._max_phases = max_phases
        self._current_phase = 1
        self._phase_abilities = {1: [], 2: [], 3: []}
        self._phase_thresholds = {}  # e.g. {2: 0.6, 3: 0.3} = 60% and 30% HP
        self._minions = []
        self._has_enraged = False

    def set_phase_abilities(self, phase, abilities):
        self._phase_abilities[phase] = abilities

    def set_phase_thresholds(self, thresholds: dict):
        self._phase_thresholds = thresholds

    def check_phase_transition(self):
        hp_percent = self._hp / self._max_hp
        for phase, threshold in self._phase_thresholds.items():
            if hp_percent <= threshold and self._current_phase < phase:
                self._current_phase = phase
                self.on_phase_change(phase)

    def on_phase_change(self, phase):
        # override in subclasses like TaraKane
        pass

    def notify_minion_death(self, minion):
        if minion in self._minions:
            self._minions.remove(minion)
        self.on_minion_death(minion)

    def on_minion_death(self, minion):
        # override in subclasses
        pass

    def add_minion(self, minion):
        self._minions.append(minion)

    @property
    def has_enraged(self):
        return self._has_enraged

    @property
    def minions_alive(self):
        return [m for m in self._minions if m.is_alive()]

    # boss.py
    def remove_phase_ability(self, phase, ability_name):
        self._phase_abilities[phase] = [
            a for a in self._phase_abilities[phase]
            if a.name != ability_name
        ]

    # boss.py - override act for Tara Kane specifically
    def act(self, battle_session):
        abilities = self._phase_abilities.get(self._current_phase, [])
        if abilities:
            # prioritize summon if available
            ability = random.choice(abilities)
            targets = battle_session.get_player_party().alive_members()
            ability.execute(self, targets, battle_session)