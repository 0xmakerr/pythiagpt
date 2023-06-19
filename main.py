import os
from dotenv import load_dotenv
from pythgpt import pyth_gpt
from discordbot import DiscordClient, discord, send_message

load_dotenv()
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')


def run():
    client = DiscordClient()

    @client.tree.command(name="chat", description="Have a chat with PythGPT")
    async def chat(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        receive = pyth_gpt(message=message)
        await send_message(interaction, message, receive)

    client.run(DISCORD_API_KEY)


run()
