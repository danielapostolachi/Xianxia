# effects.py
import random

def apply_damage(caster, target, base_damage, battle_session):
    target.take_damage(base_damage, caster.conduit, False)
    target.charge_ult(5)
    battle_session.log_fn(f"💥 {caster.name} hits {target.name} for {base_damage} damage! ({target.hp}/{target.max_hp} HP)")
    battle_session.check_entity_status(target)

def apply_true_damage(caster, target, base_damage, battle_session):
    target.take_damage(base_damage, caster.conduit, is_true_damage=True)
    battle_session.log_fn(f"🎯 {caster.name} deals {base_damage} TRUE damage to {target.name}! ({target.hp}/{target.max_hp} HP)")
    battle_session.check_entity_status(target)

def apply_heal(target, amount, battle_session):
    target.heal(amount)
    battle_session.log_fn(f"💚 {target.name} heals for {amount}! ({target.hp}/{target.max_hp} HP)")

def apply_shield(target, points, shield_conduit, battle_session):
    target._shield_hp = points
    target._shield_conduit = shield_conduit
    battle_session.log_fn(f"🛡️ {target.name} gains a {shield_conduit} shield for {points} points!")

def apply_status(target, status_name, duration, battle_session):
    target.status = status_name
    battle_session.register_status_timer(target, status_name, duration)
    battle_session.log_fn(f"⚠️ {target.name} is {status_name} for {duration} turns!")

def apply_dot(target, damage_per_turn, duration, battle_session):
    battle_session.register_dot(target, damage_per_turn, duration)
    battle_session.log_fn(f"🔥 {target.name} is burning for {damage_per_turn} damage over {duration} turns!")

def apply_buff(target, stat, magnitude, duration, battle_session):
    buff = {"stat": stat, "magnitude": magnitude, "duration": duration}
    target.buffs.append(buff)
    battle_session.log_fn(f"⬆️ {target.name} gains {stat} +{magnitude} for {duration} turns!")

def apply_debuff(target, stat, magnitude, duration, battle_session):
    debuff = {"stat": stat, "magnitude": magnitude, "duration": duration}
    target.debuffs.append(debuff)
    battle_session.log_fn(f"⬇️ {target.name} loses {stat} -{magnitude} for {duration} turns!")

def roll_crit(caster):
    crit_rate = getattr(caster, '_crit_rate', 20)
    roll = random.randint(1, 100)
    return roll <= crit_rate