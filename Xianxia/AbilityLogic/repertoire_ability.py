from Xianxia.AbilityLogic.ability import Ability

class RepertoireAbility(Ability):
    def __init__(self, name, description, conduit, targeting,
                 slot, cooldown=0, is_true_damage=False, effect_hook=None):
        super().__init__(name, description, conduit, targeting,
                         is_true_damage, effect_hook)
        self._slot = slot                    # "NA"/"skill"/"ult"/"talent"/"P1"/"P2"
        self._cooldown_max = cooldown
        self._cooldown_current = 0

    @property
    def cooldown(self):
        return self._cooldown_max

    @property
    def cooldown_current(self):
        return self._cooldown_current

    def is_available(self):
        return self._cooldown_current == 0

    def trigger_cooldown(self):
        self._cooldown_current = self._cooldown_max

    def tick_cooldown(self):
        if self._cooldown_current > 0:
            self._cooldown_current -= 1

    def get_info(self):
        return (f"[{self._slot}] {self._name}: {self._description} "
                f"| Cooldown: {self._cooldown_max} turns")
