from abc import ABC, abstractmethod

from Xianxia.ConduitLogic.fusionconduit import FusionConduit
from Xianxia.ConduitLogic.iconduit import IConduit
from Xianxia.ConduitLogic.physicalconduit import PhysicalConduit
from Xianxia.ConduitLogic.sorceryconduit import SorceryConduit


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