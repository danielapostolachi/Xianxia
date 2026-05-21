class PlayerParty:
    MAX_MEMBERS = 4

    def __init__(self, name=None, members=None, leader=None):
        self.name = name or "Unnamed Party"
        self.members = members or []
        self.leader = leader

    def add_member(self, character):
        if len(self.members) >= Party.MAX_MEMBERS:
            raise ValueError("Party is full! Max 4 players.")
        self.members.append(character)

    def pick_leader(self, character):
        if character not in self.members:
            raise ValueError("Leader must be a member of the party!")
        self.leader = character

    def show_party(self):
        print(f"Party: {self.name}")
        print(f"Leader: {self.leader.name if self.leader else 'None'}")
        print("Members:")
        for m in self.members:
            print(f" - {m.name}")