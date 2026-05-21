# hooks/registry.py
from Xianxia.Hooks.sou_hooks import sword_strike, firework, electric_slash, high_voltage
from Xianxia.Hooks.tarakane_hooks import needle_throw, summon_bees, enrage, queens_wrath, hive_mind
from Xianxia.Hooks.bee_hooks import sting, frenzy, sacrifice

HOOK_REGISTRY = {
    "sword_strike": sword_strike,
    "firework": firework,
    "electric_slash": electric_slash,
    "high_voltage": high_voltage,
    "needle_throw": needle_throw,
    "summon_bees": summon_bees,
    "enrage": enrage,
    "queens_wrath": queens_wrath,
    "hive_mind": hive_mind,
    "sting": sting,
    "frenzy": frenzy,
    "sacrifice": sacrifice,
}