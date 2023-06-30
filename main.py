import os
import asyncio
from dotenv import load_dotenv
from pythgpt import pyth_gpt, thread_lock
from discordbot import DiscordClient, discord, send_message, send_timeout

load_dotenv()
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')


def run():
    client = DiscordClient()

    @client.tree.command(name="chat", description="Ask Pythia a question")
    async def chat(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        if not thread_lock.locked():
            receive = await asyncio.to_thread(pyth_gpt, message=message)
            await send_message(interaction, message, receive)
        else:
            await send_timeout(interaction)

    client.run(DISCORD_API_KEY)


run()
