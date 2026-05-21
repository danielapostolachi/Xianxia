# party.py
class Party:
    def __init__(self, max_size=4):
        self._members = []
        self._max_size = max_size

    def add_member(self, entity):
        if len(self._members) >= self._max_size:
            print(f"Party is full! Max size is {self._max_size}")
            return False
        self._members.append(entity)
        return True

    def remove_member(self, entity):
        if entity in self._members:
            self._members.remove(entity)

    def alive_members(self):
        return [m for m in self._members if m.is_alive()]

    def all_dead(self):
        return all(not m.is_alive() for m in self._members)

    def get_members(self):
        return self._members

    @property
    def size(self):
        return len(self.alive_members())

    def __iter__(self):
        return iter(self._members)

    def __len__(self):
        return len(self._members)