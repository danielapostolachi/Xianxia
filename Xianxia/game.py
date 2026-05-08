from Xianxia.gamememento import GameMemento


class Game:
    def __init__(self):
        self.state = {}

    def save(self):
        return GameMemento(self.state.copy())

    def load(self, memento):
        self.state = memento.state.copy()