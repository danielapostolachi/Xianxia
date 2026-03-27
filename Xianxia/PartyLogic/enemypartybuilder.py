# enemy_party_builder.py
from Xianxia.PartyLogic.enemyparty import EnemyParty
from Xianxia.PartyLogic.abstractpartybuilder import AbstractPartyBuilder

class EnemyPartyBuilder(AbstractPartyBuilder):
    def __init__(self):
        self._name = None
        self._members = []
        self._leader = None

    def set_name(self, name=None):
        self._name = name or "Enemy Party"
        return self

    def add_member(self, boss_template):
        """Clone a boss template (Prototype)"""
        self._members.append(boss_template.clone())
        return self

    def add_auto_members(self, boss_templates):
        for tpl in boss_templates[:EnemyParty.MAX_MEMBERS]:
            self.add_member(tpl)
        return self

    def set_leader(self, boss_template=None):
        if not self._leader and self._members:
            self._leader = self._members[0]
        return self

    def build(self):
        return EnemyParty(self._name or "Enemy Party", self._members, self._leader)