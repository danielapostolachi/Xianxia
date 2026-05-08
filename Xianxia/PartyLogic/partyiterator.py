class PartyIterator:
    def __init__(self, members):
        self.members = members
        self.index = 0

    def __next__(self):
        if self.index >= len(self.members):
            raise StopIteration
        val = self.members[self.index]
        self.index += 1
        return val