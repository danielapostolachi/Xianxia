from Xianxia.AbilityLogic.ability import Ability

class BossAbility(Ability):
    def __init__(self, name, description, conduit, targeting,
                 phase=1, trigger="on_turn",
                 is_true_damage=False, effect_hook=None):
        super().__init__(name, description, conduit, targeting,
                         is_true_damage, effect_hook)
        self._phase = phase          # which phase this belongs to
        self._trigger = trigger      # "on_turn"/"on_hit"/"on_minion_death"/"always"

    @property
    def phase(self):
        return self._phase

    @property
    def trigger(self):
        return self._trigger

    def get_info(self):
        return (f"[Phase {self._phase}] {self._name}: {self._description} "
                f"| Trigger: {self._trigger}")