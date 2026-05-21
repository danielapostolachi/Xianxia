# factories/player_factory.py
import json
import os
from Xianxia.CombatEntities.player import Player
from Xianxia.AbilityLogic.repertoire_ability import RepertoireAbility
from Xianxia.AbilityLogic.ultimate_ability import UltimateAbility
from Xianxia.Hooks.registry import HOOK_REGISTRY

class PlayerFactory:
    def __init__(self):
        self._base_dir = os.path.dirname(os.path.abspath(__file__))

    def build(self, character_id):
        data = self._load_json(f"characters/{character_id}.json")

        player = Player(
            name=data["name"],
            hp=data["hp"],
            conduit=data["conduit"],
            speed=data["speed"],
            aspect=data["aspect"],
            aspect_category=data["aspect_category"]
        )

        player._crit_rate = data.get("crit_rate", 20)

        na = self._make_repertoire_ability(data["na"])
        skill = self._make_repertoire_ability(data["skill"])
        ult = self._make_ultimate_ability(data["ult"])
        p1 = self._make_repertoire_ability(data["passive_1"]) if data.get("passive_1") else None
        talent = self._make_repertoire_ability(data["talent"]) if data.get("talent") else None
        p2 = self._make_repertoire_ability(data["passive_2"]) if data.get("passive_2") else None

        player.set_repertoire(na=na, skill=skill, ult=ult, talent=talent, p1=p1, p2=p2)
        return player

    @staticmethod
    def _make_repertoire_ability(data):
        if not data:
            return None
        return RepertoireAbility(
            name=data["name"],
            description=data["description"],
            conduit=data["conduit"],
            targeting=data["targeting"],
            slot=data.get("slot", "NA"),
            cooldown=data.get("cooldown", 0),
            is_true_damage=data.get("is_true_damage", False),
            effect_hook=HOOK_REGISTRY.get(data["effect_hook"])
        )

    @staticmethod
    def _make_ultimate_ability(data):
        if not data:
            return None
        return UltimateAbility(
            name=data["name"],
            description=data["description"],
            conduit=data["conduit"],
            targeting=data["targeting"],
            is_true_damage=data.get("is_true_damage", False),
            effect_hook=HOOK_REGISTRY.get(data["effect_hook"])
        )

    def _load_json(self, filename):
        path = os.path.join(self._base_dir, '..', 'data', filename)
        with open(path) as f:
            return json.load(f)