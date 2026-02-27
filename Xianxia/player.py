import random

from Xianxia.character import Character
from Xianxia.AspectLogic.iaspect import IAspect
from Xianxia.ConduitLogic.iconduit import IConduit


class Player(Character):
    def __init__(self, name, hp, conduit: IConduit, aspect: IAspect, repertoire):
        super().__init__(name, hp)
        self._conduit = conduit
        self._aspect = aspect
        self._repertoire = repertoire

    def attack(self):
        ability = random.choice(self._repertoire)
        damage = random.randint(1, 20)
        return ability, damage