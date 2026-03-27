from abc import ABC, abstractmethod
import copy

class Character(ABC):
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
        self._alive = True

    @property
    def name(self):
        return self._name

    def take_damage(self, damage):
        self._hp -= damage
        if self._hp <= 0:
            self._alive = False

    def is_alive(self):
        return self._alive

    def get_hp(self):
        return self._hp

    def clone(self):
        return copy.deepcopy(self)

    @abstractmethod
    def attack(self):
        pass