from pythgpt import pyth_gpt
from discordbot import DiscordClient, Sender, discord


def run():
    client = DiscordClient()
    sender = Sender()

    @client.tree.command(name="chat", description="Have a chat with ChatGPT")
    async def chat(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        receive = pyth_gpt(message=message)
        await sender.send_message(interaction, message, receive)

    client.run('YOUR DISCORD TOKEN')


run()
