from abc import ABC, abstractmethod

class Ability(ABC):
    def __init__(self, name, description, conduit, targeting,
                 is_true_damage=False, effect_hook=None):
        self._name = name
        self._description = description
        self._conduit = conduit        # "physical"/"sorcery"/"fusion"/"none"
        self._targeting = targeting    # "single"/"aoe"/"self"/"ally"
        self._is_true_damage = is_true_damage
        self._effect_hook = effect_hook

    @property
    def name(self):
        return self._name

    @property
    def targeting(self):
        return self._targeting

    @property
    def is_true_damage(self):
        return self._is_true_damage

    @property
    def conduit(self):
        return self._conduit

    def execute(self, caster, targets, battle_session):
        if self._effect_hook:
            self._effect_hook(caster, targets, battle_session)

    @abstractmethod
    def get_info(self):
        pass
