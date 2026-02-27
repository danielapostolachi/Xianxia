from abc import ABC, abstractmethod
from Xianxia.AspectLogic.iaspect import IAspect

class AspectFactory(ABC):

    @abstractmethod
    def create_aspect(self, subrole: str) -> IAspect:
        pass