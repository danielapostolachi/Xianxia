from abc import ABC, abstractmethod
from Xianxia.ConduitLogic.conduit import PhysicalConduit, SorceryConduit, FusionConduit
from Xianxia.ConduitLogic.iconduit import IConduit

class ConduitFactory(ABC):
    @abstractmethod
    def create_conduit(self, name: str) -> IConduit:
        pass

class PhysicalFactory(ConduitFactory):
    def create_conduit(self, name: str) -> IConduit:
        return PhysicalConduit(name)

class SorceryFactory(ConduitFactory):
    def create_conduit(self, name: str) -> IConduit:
        return SorceryConduit(name)

class FusionFactory(ConduitFactory):
    def create_conduit(self, name: str) -> IConduit:
        return FusionConduit(name)