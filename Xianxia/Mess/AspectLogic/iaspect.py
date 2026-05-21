from abc import ABC, abstractmethod

class IAspect(ABC):
    @abstractmethod
    def get_role(self) -> str:
        pass

    @abstractmethod
    def get_subrole(self) -> str:
        pass