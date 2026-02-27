import random

from Xianxia.character import Character

class Boss(Character):
    def __init__(self, name, hp, attacks):
        super().__init__(name, hp)
        self._attacks = attacks

    def attack(self):
            attack_name = random.choice(self._attacks)
            damage = random.randint(1, 20)
            return attack_name, damage
