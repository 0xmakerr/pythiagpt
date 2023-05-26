import os
from dotenv import load_dotenv
from pythgpt import pyth_gpt
from discordbot import DiscordClient, Sender, discord

load_dotenv()
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')
MAX_MESSAGE_LENGTH = 1900


def run():
    client = DiscordClient()
    sender = Sender()

    @client.tree.command(name="chat", description="Have a chat with PythGPT")
    async def chat(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        receive = pyth_gpt(message=message)
        if len(receive) <= MAX_MESSAGE_LENGTH:
            await sender.send_message(interaction, message, receive)
        else:
            last_space_index = receive[:MAX_MESSAGE_LENGTH].rfind(" ")
            await sender.send_message(interaction, message, receive[:last_space_index])
            await sender.send_message(interaction, message, receive[last_space_index + 1:])

    client.run(DISCORD_API_KEY)


run()
