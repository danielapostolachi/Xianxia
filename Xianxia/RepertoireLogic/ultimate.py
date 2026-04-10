from Xianxia.RepertoireLogic.ability import Ability


class Ultimate(Ability):
    def execute(self, user, target, game_state):
        if user.ultimate_charge >= 100:
            game_state.interrupt_turn_order(user)
            user.ultimate_charge = 0
            return user.conduit.deal_damage(user, target) * 3