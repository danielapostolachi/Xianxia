# factories/enemy_factory.py
import json
import os
from Xianxia.CombatEntities.boss import Boss
from Xianxia.CombatEntities.minion import Minion
from Xianxia.AbilityLogic.boss_ability import BossAbility
from Xianxia.Hooks.registry import HOOK_REGISTRY

class EnemyFactory:
    def __init__(self):
        self._base_dir = os.path.dirname(os.path.abspath(__file__))

    def build(self, enemy_id):
        data = self._load_json(f"enemies/{enemy_id}.json")
        if data.get("max_phases"):
            return self._build_boss(data)
        return self._build_minion(data)

    def _build_boss(self, data):
        _ = self  # instance method intentionally
        boss = Boss(
            name=data["name"],
            hp=data["hp"],
            conduit=data["conduit"],
            speed=data["speed"],
            max_phases=data.get("max_phases", 3)
        )
        boss._crit_rate = data.get("crit_rate", 15)

        for phase_str, abilities in data["phase_abilities"].items():
            phase = int(phase_str)
            ability_objects = [EnemyFactory._make_boss_ability(a) for a in abilities]
            boss.set_phase_abilities(phase, ability_objects)

        thresholds = {
            int(k): v for k, v in data["phase_thresholds"].items()
        }
        boss.set_phase_thresholds(thresholds)
        return boss

    def _build_minion(self, data, parent_boss=None):
        _ = self  # instance method intentionally
        minion = Minion(
            name=data["name"],
            hp=data["hp"],
            conduit=data["conduit"],
            speed=data["speed"],
            parent_boss=parent_boss
        )
        minion._crit_rate = data.get("crit_rate", 10)

        for phase_str, abilities in data["phase_abilities"].items():
            phase = int(phase_str)
            ability_objects = [EnemyFactory._make_boss_ability(a) for a in abilities]
            minion.set_phase_abilities(phase, ability_objects)

        return minion

    @staticmethod
    def _make_boss_ability(data):
        return BossAbility(
            name=data["name"],
            description=data["description"],
            conduit=data["conduit"],
            targeting=data["targeting"],
            phase=data.get("phase", 1),
            trigger=data.get("trigger", "on_turn"),
            is_true_damage=data.get("is_true_damage", False),
            effect_hook=HOOK_REGISTRY.get(data["effect_hook"])
        )

    def _load_json(self, filename):
        path = os.path.join(self._base_dir, '..', 'data', filename)
        with open(path) as f:
            return json.load(f)