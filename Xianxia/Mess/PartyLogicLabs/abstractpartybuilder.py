from abc import ABC, abstractmethod

class AbstractPartyBuilder(ABC):
    @abstractmethod
    def set_name(self, name): pass

    @abstractmethod
    def add_member(self, character): pass

    @abstractmethod
    def set_leader(self, character): pass

    @abstractmethod
    def build(self): pass