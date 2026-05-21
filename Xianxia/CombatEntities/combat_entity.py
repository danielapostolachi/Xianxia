from abc import ABC, abstractmethod
import copy


class CombatEntity(ABC):
    def __init__(self, name, hp, conduit, speed=10):
        self._name = name
        self._max_hp = hp
        self._hp = hp
        self._conduit = conduit
        self._speed = speed
        self._status = "alive"
        self._shield_hp = 0
        self._shield_conduit = None
        self._energy = 0  # 0-100, replaces _energy
        self._max_energy = 100
        self._ult_ready = False
        self._buffs = []
        self._debuffs = []

    def charge_ult(self, amount):
        self._energy = min(self._energy + amount, self._max_energy)
        if self._energy >= 100:
            self._ult_ready = True

    @property
    def name(self):
        return self._name

    @property
    def speed(self):
        return self._speed

    @property
    def hp(self):
        return self._hp

    @property
    def conduit(self):
        return self._conduit

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def max_hp(self):
        return self._max_hp

    def take_damage(self, damage, damage_conduit, is_true_damage=False):
        if is_true_damage:
            self._hp -= damage
        elif self._shield_hp > 0:
            self._process_shield_damage(damage, damage_conduit)
        else:
            self._hp -= damage

        if self._hp <= 0:
            self._hp = 0
            self._status = "dead"

    def _process_shield_damage(self, damage, damage_conduit):
        pass  # you'll fill this in when you write the damage pipeline

    def heal(self, amount):
        self._hp = min(self._hp + amount, self._max_hp)

    def is_alive(self):
        return self._status != "dead"

    # in combat_entity.py
    @property
    def buffs(self):
        return self._buffs

    @property
    def debuffs(self):
        return self._debuffs

    # combat_entity.py
    @property
    def shield_hp(self):
        return self._shield_hp

    @abstractmethod
    def act(self, battle_session):
        pass