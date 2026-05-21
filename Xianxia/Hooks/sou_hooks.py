# hooks/sou_hooks.py
from Xianxia.AbilityLogic.effects import apply_damage, apply_dot, apply_status, roll_crit

def sword_strike(caster, targets, battle_session):
    target = targets[0]
    battle_session.log_fn(f"⚔️ {caster.name} uses Sword Strike!")
    apply_damage(caster, target, 50, battle_session)
    if roll_crit(caster) and target.shield_hp == 0:
        battle_session.log_fn(f"💢 Critical hit! {target.name} is wounded!")
        apply_status(target, "wounded", 2, battle_session)

def firework(caster, targets, battle_session):
    target = targets[0]
    battle_session.log_fn(f"🎆 {caster.name} uses Firework!")
    apply_dot(target, 20, 2, battle_session)
    apply_status(target, "disoriented", 1, battle_session)
    caster._na_mode = "aoe"

def electric_slash(caster, targets, battle_session):
    battle_session.log_fn(f"⚡ {caster.name} uses Electric Slash!")
    firework_active = any(t.status == "disoriented" for t in targets)
    multiplier = 1.5 if firework_active else 1.0
    if firework_active:
        battle_session.log_fn(f"🔋 High Voltage triggered! {multiplier}x damage!")
    base_damage = 120
    for target in targets:
        apply_damage(caster, target, int(base_damage * multiplier), battle_session)

def high_voltage(caster, targets, battle_session):
    _ = caster, targets, battle_session
    pass