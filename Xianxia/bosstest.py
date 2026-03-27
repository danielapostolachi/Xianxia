from Xianxia.boss import Boss
from Xianxia.bossregistry import BossRegistry

# Create original boss template
dragon_boss = Boss(
    "Dragon Emperor",
    500,
    ["Celestial Flame", "Dragon Tail", "Heavenly Roar"]
)

print("Original boss HP:", dragon_boss.get_hp())

# Setup Boss Registry (Prototype manager)
registry = BossRegistry()
registry.register("dragon", dragon_boss)

# Spawn clones
boss1 = registry.spawn("dragon")
boss2 = registry.spawn("dragon")

print("\nAfter cloning:")
print("Boss1 HP:", boss1.get_hp())
print("Boss2 HP:", boss2.get_hp())
print("Original template HP:", dragon_boss.get_hp())

# Modify a clone
boss1.take_damage(120)
print("\nAfter dealing 120 damage to Boss1:")
print("Boss1 HP:", boss1.get_hp())          # 380
print("Boss2 HP:", boss2.get_hp())          # 500
print("Original template HP:", dragon_boss.get_hp())  # 500

# Check that attack works
ability, damage = boss1.attack()
print(f"\nBoss1 attacks with {ability} for {damage} damage!")