class Ability:
    def __init__(self, damage_impl):
        self.damage_impl = damage_impl

    def execute(self, user, target, game_state):
        pass