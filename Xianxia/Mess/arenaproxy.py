# arena_proxy.py
from Xianxia.Mess.arena import Arena

class ArenaProxy:
    def __init__(self):
        self._arena = Arena()

    def start_battle(self, party, boss):
        # Access control logic
        if not party.members:
            print("[Proxy] Cannot start battle: party is empty!")
            return

        if not boss.is_alive():
            print("[Proxy] Boss is already dead!")
            return

        print("[Proxy] Access granted to Arena")
        self._arena.start_battle(party, boss)