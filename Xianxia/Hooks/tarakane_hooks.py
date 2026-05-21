# hooks/tarakane_hooks.py
from Xianxia.AbilityLogic.effects import apply_damage, apply_dot, apply_status, roll_crit

def needle_throw(caster, targets, battle_session):
    target = targets[0]
    battle_session.log_fn(f"🪡 {caster.name} uses Needle Throw!")
    apply_damage(caster, target, 40, battle_session)
    if roll_crit(caster) and target.shield_hp == 0:
        battle_session.log_fn(f"💢 Critical hit! {target.name} is stunned!")
        apply_status(target, "stunned", 2, battle_session)

def summon_bees(caster, targets, battle_session):
    _ = targets
    if len(caster.minions_alive) > 0:
        battle_session.log_fn(f"🐝 The bees are already here!")
        return
    if battle_session.get_enemy_party().size >= 5:
        battle_session.log_fn(f"🐝 No room for more bees!")
        return

    from Xianxia.CombatEntities.minion import Minion
    from Xianxia.Hooks.bee_hooks import sting, frenzy, sacrifice
    from Xianxia.AbilityLogic.boss_ability import BossAbility

    battle_session.log_fn(f"🐝 {caster.name} summons the swarm!")

    for i in range(4):
        bee = Minion(
            name=f"Bee {i + 1}",
            hp=150,
            conduit="sorcery",
            speed=8,
            parent_boss=caster
        )
        bee_sting = BossAbility(
            name="Sting", description="A quick sting.",
            conduit="sorcery", targeting="single",
            phase=1, trigger="on_turn", effect_hook=sting
        )
        bee_frenzy = BossAbility(
            name="Frenzy", description="Multiple stings.",
            conduit="sorcery", targeting="single",
            phase=1, trigger="on_turn", effect_hook=frenzy
        )
        bee_sacrifice = BossAbility(
            name="Sacrifice", description="One massive sting. Bee dies after.",
            conduit="sorcery", targeting="single",
            phase=1, trigger="on_turn", effect_hook=sacrifice
        )
        bee.set_phase_abilities(1, [bee_sting, bee_frenzy, bee_sacrifice])
        caster.add_minion(bee)
        battle_session.add_enemy(bee)

    # replace the last block
    caster.remove_phase_ability(1, "Summon Bees")

def enrage(caster, targets, battle_session):
    if caster.has_enraged:
        needle_throw(caster, targets, battle_session)
        return
    caster._has_enraged = True
    battle_session.log_fn(f"😡 {caster.name} ENRAGES!")
    apply_status(caster, "enraged", 999, battle_session)
    for target in targets:
        apply_dot(target, 15, 2, battle_session)

def queens_wrath(caster, targets, battle_session):
    battle_session.log_fn(f"👑 {caster.name} uses Queen's Wrath!")
    for target in targets:
        apply_damage(caster, target, 200, battle_session)

def hive_mind(caster, targets, battle_session):
    _ = caster, targets, battle_session
    pass