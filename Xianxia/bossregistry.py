class BossRegistry:
    def __init__(self):
        self._templates = {}

    def register(self, key, boss):
        self._templates[key] = boss

    def spawn(self, key):
        return self._templates[key].clone()