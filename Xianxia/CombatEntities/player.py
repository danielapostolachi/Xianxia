# player.py
from Xianxia.CombatEntities.combat_entity import CombatEntity

class Player(CombatEntity):
    def __init__(self, name, hp, conduit, speed, aspect, aspect_category):
        super().__init__(name, hp, conduit, speed)
        self._aspect = aspect
        self._aspect_category = aspect_category
        self._na = None
        self._skill = None
        self._ult = None
        self._talent = None
        self._passive_1 = None
        self._passive_2 = None

    @property
    def aspect(self):
        return self._aspect

    def set_repertoire(self, na, skill, ult, talent=None, p1=None, p2=None):
        self._na = na
        self._skill = skill
        self._ult = ult
        self._talent = talent
        self._passive_1 = p1
        self._passive_2 = p2

    # def act(self, battle_session):
        # for demo: Discord will call these directly
        # this is a placeholder for now
     #   pass

    def gain_ult_charge(self, amount):
        self.charge_ult(amount)

    def use_normal_attack(self, targets, battle_session):
        if self._na:
            self._na.execute(self, targets, battle_session)
            self.gain_ult_charge(10)

    def use_skill(self, targets, battle_session):
        if self._skill and self._skill.is_available():
            self._skill.execute(self, targets, battle_session)
            charge = 5 + (10 * self._skill.cooldown)
            self.gain_ult_charge(charge)
            self._skill.trigger_cooldown()

    def use_ultimate(self, targets, battle_session):
        if self._ult_ready:
            self._ult.execute(self, targets, battle_session)
            self._energy = 0
            self._ult_ready = False

    def check_ult_ready(self):
        return self._ult_ready


    @property
    def skill(self):
        return self._skill

    # player.py - temporary AI for testing
    def act(self, battle_session):
        enemies = battle_session.get_enemy_party().alive_members()
        if not enemies:
            return
        if self._ult_ready:
            self.use_ultimate(enemies, battle_session)
        elif self._skill and self._skill.is_available():
            self.use_skill([enemies[0]], battle_session)
        else:
            self.use_normal_attack([enemies[0]], battle_session)

    @property
    def na_mode(self):
        return self._na_mode if hasattr(self, '_na_mode') else "single"

    @property
    def energy(self):
        return self._energy

    @property
    def ult_ready(self):
        return self._ult_ready