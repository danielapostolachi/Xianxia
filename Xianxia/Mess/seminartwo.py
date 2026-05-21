# ==============================
# REAL OBJECT (Heavy Enemy)
# ==============================
class Enemy:
    def __init__(self):
        print("[Enemy] Loading heavy assets (textures, stats, AI)...")
        self.hp = 100

    def take_damage(self, dmg):
        self.hp -= dmg
        print(f"[Enemy] Took {dmg} damage. HP = {self.hp}")


# ==============================
# REMOTE PROXY (Simulates server)
# ==============================
class RemoteProxy:
    def send_damage(self, dmg):
        print(f"[RemoteProxy] Sending damage ({dmg}) to server...")
        print("[RemoteProxy] Server processed request ✔")


# ==============================
# MAIN PROXY (combines all 3)
# ==============================
class EnemyProxy:
    def __init__(self, player_level):
        self._real_enemy = None   # Virtual Proxy (lazy loading)
        self._player_level = player_level
        self._remote = RemoteProxy()  # Remote Proxy

    def take_damage(self, dmg):
        # 🔐 PROTECTION PROXY
        if self._player_level < 3:
            print("[ProtectionProxy] Player level too low to damage this enemy!")
            return

        # 💤 VIRTUAL PROXY
        if self._real_enemy is None:
            print("[VirtualProxy] Creating enemy only now...")
            self._real_enemy = Enemy()

        # 🌐 REMOTE PROXY
        self._remote.send_damage(dmg)

        # Forward request to real object
        self._real_enemy.take_damage(dmg)


# ==============================
# GAME SIMULATION
# ==============================
def main():
    print("=== Scenario 1: Weak player tries to attack ===")
    weak_player_enemy = EnemyProxy(player_level=1)
    weak_player_enemy.take_damage(20)

    print("\n=== Scenario 2: Strong player attacks ===")
    strong_player_enemy = EnemyProxy(player_level=5)

    # First attack → triggers lazy loading
    strong_player_enemy.take_damage(30)

    # Second attack → enemy already exists
    strong_player_enemy.take_damage(25)


if __name__ == "__main__":
    main()