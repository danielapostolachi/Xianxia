from Xianxia.iaspect import IAspect

class Aspect(IAspect):
    def __init__(self, role: str, subrole: str):
        self._role = role
        self._subrole = subrole

    def get_role(self) -> str:
        return self._role

    def get_subrole(self) -> str:
        return self._subrole