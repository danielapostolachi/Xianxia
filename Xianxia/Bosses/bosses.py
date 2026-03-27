from Xianxia.boss import Boss

# Original template
dragon_boss = Boss(
    "Dragon Emperor",
    500,
    ["Celestial Flame", "Dragon Tail", "Heavenly Roar"]
)

# Clones
boss1 = dragon_boss.clone()
boss2 = dragon_boss.clone()

# Modify a clone safely
boss1.take_damage(100)

print(boss1.get_hp())      # 400
print(boss2.get_hp())      # 500
print(dragon_boss.get_hp()) # 500