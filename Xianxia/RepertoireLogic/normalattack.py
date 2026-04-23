from Xianxia.RepertoireLogic.ability import Ability


class NormalAttack(Ability):
    def execute(self, user, target, game_state):
        damage = self.damage_impl.calculate(user, target)
        user.energy += 10
        return damage