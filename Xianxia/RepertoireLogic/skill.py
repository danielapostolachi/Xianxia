from Xianxia.RepertoireLogic.ability import Ability


class Skill(Ability):
    def execute(self, user, target, game_state):
        damage = user.conduit.deal_damage(user, target) * 1.5
        user.energy += 5 + (10 * self.cooldown_turns)
        return damage