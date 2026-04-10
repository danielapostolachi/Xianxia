from Xianxia.ConduitLogic.conduit import Conduit
from Xianxia.ConduitLogic.physicalconduit import PhysicalConduit
from Xianxia.ConduitLogic.sorceryconduit import SorceryConduit


class FusionConduit(Conduit):
    def __init__(self, name: str):
        super().__init__(name, "Fusion")
        self._mode = "Physical"
        self._physical = PhysicalConduit(name + "_phys")
        self._sorcery = SorceryConduit(name + "_sorc")

    def switch_mode(self):
        self._mode = "Sorcery" if self._mode == "Physical" else "Physical"

    def _current(self):
        return self._physical if self._mode == "Physical" else self._sorcery

    # ADAPT calls to current system
    def deal_damage(self, attacker, target) -> float:
        return self._current().deal_damage(attacker, target)

    def apply_effect(self, attacker, target):
        self._current().apply_effect(attacker, target)

    def break_shield(self, target):
        self._current().break_shield(target)