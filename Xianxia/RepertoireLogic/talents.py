from Xianxia.RepertoireLogic.ability import Ability


class TalentDecorator(Ability):
    def __init__(self, ability):
        self.ability = ability

    def execute(self, user, target, game_state):
        base = self.ability.execute(user, target, game_state)
        return base * 1.2  # modify behavior