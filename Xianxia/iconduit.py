from abc import ABC, abstractmethod

class IConduit(ABC):
    @abstractmethod
    def get_damage_type(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass
