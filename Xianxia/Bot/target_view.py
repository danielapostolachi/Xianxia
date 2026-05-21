# bot/target_view.py
import discord
import asyncio

class TargetView(discord.ui.View):
    def __init__(self, enemies, timeout=30):
        super().__init__(timeout=timeout)
        self.chosen_target = None

        for i, enemy in enumerate(enemies):
            button = discord.ui.Button(
                label=f"{enemy.name} ({enemy.hp}/{enemy.max_hp} HP)",
                style=discord.ButtonStyle.danger,
                custom_id=str(i)
            )
            button.callback = self._make_callback(i, enemy)
            self.add_item(button)

    def _make_callback(self, index, enemy):
        async def callback(interaction: discord.Interaction):
            self.chosen_target = enemy
            await interaction.response.defer()
            self.stop()
        return callback