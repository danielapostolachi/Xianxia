# hooks/bee_hooks.py
from Xianxia.AbilityLogic.effects import apply_damage

def sting(caster, targets, battle_session):
    target = targets[0]
    battle_session.log_fn(f"🐝 {caster.name} stings {target.name}!")
    apply_damage(caster, target, 30, battle_session)

def frenzy(caster, targets, battle_session):
    target = targets[0]
    battle_session.log_fn(f"🐝 {caster.name} goes into a frenzy!")
    for _ in range(3):
        apply_damage(caster, target, 20, battle_session)

def sacrifice(caster, targets, battle_session):
    target = targets[0]
    battle_session.log_fn(f"💀 {caster.name} sacrifices itself!")
    apply_damage(caster, target, 120, battle_session)
    caster._hp = 0
    caster._status = "dead"