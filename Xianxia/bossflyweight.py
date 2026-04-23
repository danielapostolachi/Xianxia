# boss_flyweight.py
from Xianxia.boss import Boss

class BossFlyweightFactory:
    _boss_pool = {}

    @staticmethod
    def get_boss(name, hp, attacks):
        key = (name, hp, tuple(attacks))

        if key not in BossFlyweightFactory._boss_pool:
            print(f"[Flyweight] Creating new boss: {name}")
            BossFlyweightFactory._boss_pool[key] = Boss(name, hp, attacks)
        else:
            print(f"[Flyweight] Reusing existing boss: {name}")

        return BossFlyweightFactory._boss_pool[key]