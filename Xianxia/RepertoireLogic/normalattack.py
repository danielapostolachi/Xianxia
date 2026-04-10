from Xianxia.RepertoireLogic.ability import Ability


class NormalAttack(Ability):
    def execute(self, user, target, game_state):
        damage = user.conduit.deal_damage(user, target)
        user.energy += 10
        return damage