# ==============================
# FLYWEIGHT (Shared data)
# ==============================
class EnemyType:
    def __init__(self, name, base_hp, texture):
        self.name = name
        self.base_hp = base_hp
        self.texture = texture

    def render(self, x, y):
        print(f"[Render] {self.name} at ({x}, {y}) using {self.texture}")


# ==============================
# FLYWEIGHT FACTORY (Cache)
# ==============================
class EnemyFactory:
    _types = {}

    @classmethod
    def get_enemy_type(cls, name):
        if name not in cls._types:
            print(f"[Factory] Creating new enemy type: {name}")
            if name == "orc":
                cls._types[name] = EnemyType("orc", 100, "orc.png")
            elif name == "elf":
                cls._types[name] = EnemyType("elf", 70, "elf.png")
            else:
                cls._types[name] = EnemyType(name, 50, "default.png")

        return cls._types[name]


# ==============================
# CONTEXT OBJECT (uses flyweight)
# ==============================
class Enemy:
    def __init__(self, enemy_type, x, y):
        self.type = enemy_type  # shared
        self.x = x              # unique
        self.y = y              # unique
        self.hp = enemy_type.base_hp  # copied but could be extrinsic too

    def render(self):
        self.type.render(self.x, self.y)

    def take_damage(self, dmg):
        self.hp -= dmg
        print(f"[Enemy] {self.type.name} HP = {self.hp}")


# ==============================
# GAME SIMULATION
# ==============================
def main():
    enemies = []

    # Creating many enemies of same type
    for i in range(5):
        enemy_type = EnemyFactory.get_enemy_type("orc")
        enemies.append(Enemy(enemy_type, x=i * 10, y=0))

    # Creating different type
    elf_type = EnemyFactory.get_enemy_type("elf")
    enemies.append(Enemy(elf_type, x=50, y=20))

    print("\n--- Rendering ---")
    for e in enemies:
        e.render()

    print("\n--- Damage ---")
    enemies[0].take_damage(20)


if __name__ == "__main__":
    main()