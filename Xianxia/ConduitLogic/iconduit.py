from abc import ABC, abstractmethod

class IConduit(ABC):
    @abstractmethod
    def get_damage_type(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def deal_damage(self, attacker, target) -> float:
        pass

    @abstractmethod
    def apply_effect(self, attacker, target):
        pass

    @abstractmethod
    def break_shield(self, target):
        pass