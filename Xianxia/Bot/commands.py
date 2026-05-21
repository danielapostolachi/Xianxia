# bot/commands.py
import discord
from discord import app_commands
from discord.ext import commands
from Xianxia.Bot.target_view import TargetView
from Xianxia.Factories.player_factory import PlayerFactory
from Xianxia.Factories.enemy_factory import EnemyFactory
from Xianxia.BattleLogic.party import Party
from Xianxia.BattleLogic.battle_session import BattleSession
from Xianxia.Bot.battle_embed import build_battle_embed
import asyncio

active_battles = {}

class BattleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="fight", description="Start a battle!")
    @app_commands.describe(enemy="Enemy to fight (e.g. tara_kane)")
    async def fight(self, interaction: discord.Interaction, enemy: str):
        channel_id = interaction.channel_id

        if channel_id in active_battles:
            await interaction.response.send_message(
                "⚔️ A battle is already active in this channel!", ephemeral=True
            )
            return

        try:
            sou = PlayerFactory().build("sou")
            foe = EnemyFactory().build(enemy)
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Could not load enemy `{enemy}`: {e}", ephemeral=True
            )
            return

        player_party = Party(max_size=4)
        player_party.add_member(sou)
        enemy_party = Party(max_size=5)
        enemy_party.add_member(foe)

        session = BattleSession(player_party, enemy_party)
        session.roll_initiative()
        session.log_fn = lambda msg: active_battles[channel_id]["log"].append(msg)

        active_battles[channel_id] = {
            "session": session,
            "sou": sou,
            "log": []
        }

        embed = build_battle_embed(session, ["⚔️ Battle starts! Use /attack, /skill, or /ult to act!"])
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="attack", description="Use normal attack")
    async def attack(self, interaction: discord.Interaction):
        await self._player_action(interaction, "na")

    @app_commands.command(name="skill", description="Use your skill")
    async def skill(self, interaction: discord.Interaction):
        await self._player_action(interaction, "skill")

    @app_commands.command(name="ult", description="Use your ultimate")
    async def ult(self, interaction: discord.Interaction):
        await self._player_action(interaction, "ult")

    async def _get_target(self, interaction, enemies):
        _ = self
        alive = [e for e in enemies if e.is_alive()]
        view = TargetView(alive)
        await interaction.followup.send("🎯 Choose your target:", view=view)
        await view.wait()
        return view.chosen_target

    async def _player_action(self, interaction: discord.Interaction, action: str):
        channel_id = interaction.channel_id

        if channel_id not in active_battles:
            await interaction.response.send_message(
                "❌ No active battle! Start one with `/fight`", ephemeral=True
            )
            return

        await interaction.response.defer()

        data = active_battles[channel_id]
        session = data["session"]
        sou = data["sou"]

        # always refresh enemies at action time
        enemies = session.get_enemy_party().alive_members()

        # debug — remove later
        print(f"Enemy party: {[m.name for m in session.get_enemy_party().get_members()]}")
        print(f"Alive enemies: {[m.name for m in enemies]}")

        if not enemies:
            await interaction.followup.send("✅ Battle already over!")
            return

        log = []
        session.log_fn = lambda msg: log.append(msg)

        if action == "na":
            if sou.na_mode == "aoe":
                sou.use_normal_attack(enemies, session)
            else:
                enemies = session.get_enemy_party().alive_members()
                target = await self._get_target(interaction, enemies)
                if not target:
                    await interaction.followup.send("⏱️ Timed out! Turn skipped.")
                    return
                sou.use_normal_attack([target], session)

        elif action == "skill":
            if sou.skill and sou.skill.is_available():
                enemies = session.get_enemy_party().alive_members()
                target = await self._get_target(interaction, enemies)
                if not target:
                    await interaction.followup.send("⏱️ Timed out! Turn skipped.")
                    return
                sou.use_skill([target], session)
            else:
                cooldown = sou.skill.cooldown_current if sou.skill else "?"
                await interaction.followup.send(
                    f"❌ Skill on cooldown! ({cooldown} turns remaining)"
                )
                return

        elif action == "ult":
            if sou.ult_ready:
                enemies = session.get_enemy_party().alive_members()
                sou.use_ultimate(enemies, session)
            else:
                await interaction.followup.send(
                    f"❌ Ult not ready! ({sou.energy}/100)"
                )
                return

        if log:
            await interaction.followup.send("\n".join(log))
            await asyncio.sleep(1.5)

        session.check_win_condition()
        if session.is_over:
            embed = build_battle_embed(session, ["🏆 Players win!"])
            await interaction.followup.send(embed=embed)
            del active_battles[channel_id]
            return

        for entity in list(session.turn_order):
            if not entity.is_alive():
                continue
            if entity in session.get_player_party().get_members():
                continue
            if entity.status == "stunned":
                await interaction.followup.send(f"⚡ {entity.name} is stunned and skips their turn!")
                await asyncio.sleep(1.5)
                continue

            enemy_log = []
            session.log_fn = lambda msg: enemy_log.append(msg)
            entity.act(session)

            if enemy_log:
                await interaction.followup.send("\n".join(enemy_log))
                await asyncio.sleep(1.5)

            session.check_win_condition()
            if session.is_over:
                break

        tick_log = []
        session.log_fn = lambda msg: tick_log.append(msg)
        session.round += 1
        session.tick_timers()
        session.tick_cooldowns()

        if tick_log:
            await interaction.followup.send("\n".join(tick_log))
            await asyncio.sleep(1.5)

        if session.is_over:
            embed = build_battle_embed(session, ["💀 Enemies win!"])
            await interaction.followup.send(embed=embed)
            del active_battles[channel_id]
            return

        embed = build_battle_embed(session)
        await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(BattleCog(bot))