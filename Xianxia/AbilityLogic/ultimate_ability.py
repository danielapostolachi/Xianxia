from Xianxia.AbilityLogic.repertoire_ability import RepertoireAbility

class UltimateAbility(RepertoireAbility):
    def __init__(self, name, description, conduit, targeting,
                 is_true_damage=False, effect_hook=None):
        super().__init__(name, description, conduit, targeting,
                         slot="ult", cooldown=0,
                         is_true_damage=is_true_damage,
                         effect_hook=effect_hook)

    def execute(self, caster, targets, battle_session):
        if caster._ult_ready:
            super().execute(caster, targets, battle_session)
            caster._energy = 0
            caster._ult_ready = False

    def get_info(self):
        return f"[ULT] {self._name}: {self._description}"