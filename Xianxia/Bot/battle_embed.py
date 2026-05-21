# bot/battle_embed.py
import discord

def hp_bar(current, maximum, length=10):
    filled = int((current / maximum) * length)
    bar = "█" * filled + "░" * (length - filled)
    return f"`{bar}` {current}/{maximum}"

def build_battle_embed(battle_session, log_lines=None):
    embed = discord.Embed(
        title="⚔️ Battle",
        color=discord.Color.red()
    )

    # player party
    player_text = ""
    for member in battle_session.get_player_party().get_members():
        status = f" `{member.status}`" if member.status != "alive" else ""
        energy = f" ⚡{member.energy}/100"
        player_text += f"**{member.name}**{status}\n{hp_bar(member.hp, member.max_hp)}{energy}\n\n"
    embed.add_field(name="🧑 Party", value=player_text or "None", inline=True)

    # enemy party
    enemy_text = ""
    for member in battle_session.get_enemy_party().get_members():
        if member.is_alive():
            status = f" `{member.status}`" if member.status != "alive" else ""
            enemy_text += f"**{member.name}**{status}\n{hp_bar(member.hp, member.max_hp)}\n\n"
    embed.add_field(name="👾 Enemies", value=enemy_text or "None", inline=True)

    # battle log
    if log_lines:
        log_text = "\n".join(log_lines[-8:])
        embed.add_field(name="📜 Log", value=log_text, inline=False)

    embed.set_footer(text=f"Round {battle_session.round}")
    return embed