import discord

intents = discord.Intents.default()
intents.message_content = True


class DiscordClient(discord.Client):
    def __init__(self) -> None:
        super().__init__(intents=intents)
        self.synced = False
        self.added = False
        self.tree = discord.app_commands.CommandTree(self)
        self.activity = discord.Activity(type=discord.ActivityType.watching, name="/chat")

    async def on_ready(self):
        await self.wait_until_ready()
        print("Syncing")
        if not self.synced:
            await self.tree.sync()
            self.synced = True
        if not self.added:
            self.added = True
        print(f"Synced, {self.user} is running!")


class Sender:
    async def send_message(self, interaction, send, receive):
        try:
            user_id = interaction.user.id
            response = f'> **{send}** - <@{str(user_id)}> \n\n{receive}'
            await interaction.followup.send(response)
            print(f"{user_id} sent: {send}, response: {receive}")
        except Exception as e:
            await interaction.followup.send('> **Error: Something went wrong, please try again later!**')
            print(f"Error while sending:{send} in chatgpt model, error: {e}")
