class Repertoire:
    def __init__(self, normal, skill, ultimate, talent=None, passives=None):
        if talent:
            self.normal = talent(normal)
            self.skill = talent(skill)
            self.ultimate = talent(ultimate)
        else:
            self.normal = normal
            self.skill = skill
            self.ultimate = ultimate

        self.talent = talent
        self.passives = passives or []

    def get_ability(self, type):
        return {
            "normal": self.normal,
            "skill": self.skill,
            "ultimate": self.ultimate
        }[type]