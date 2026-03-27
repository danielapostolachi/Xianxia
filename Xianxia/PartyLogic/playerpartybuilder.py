# player_party_builder.py
from Xianxia.PartyLogic.playerparty import PlayerParty
from Xianxia.PartyLogic.abstractpartybuilder import AbstractPartyBuilder

class PlayerPartyBuilder(AbstractPartyBuilder):
    def __init__(self):
        self._name = None
        self._members = []
        self._leader = None

    def set_name(self, name):
        self._name = name
        return self

    def add_member(self, character):
        if len(self._members) >= PlayerParty.MAX_MEMBERS:
            raise ValueError("Cannot add more than 4 players")
        self._members.append(character)
        return self

    def add_auto_members(self, player_templates):
        """Automatically add up to 4 players"""
        for tpl in player_templates[:PlayerParty.MAX_MEMBERS]:
            self.add_member(tpl)
        return self

    def set_leader(self, character):
        self._leader = character
        return self

    def build(self):
        if self._leader is None and self._members:
            self._leader = self._members[0]
        return PlayerParty(self._name or "Player Party", self._members, self._leader)