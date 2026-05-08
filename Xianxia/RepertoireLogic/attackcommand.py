from Xianxia.RepertoireLogic.command import Command


class AttackCommand(Command):
    def __init__(self, user, target, ability):
        self.user = user
        self.target = target
        self.ability = ability

    def execute(self):
        return self.ability.execute(self.user, self.target, None)