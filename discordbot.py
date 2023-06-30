import discord
import math

intents = discord.Intents.default()
intents.message_content = True
MAX_MESSAGE_LENGTH = 1950


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


async def send_message(interaction, send, receive):
    try:
        user_id = interaction.user.id
        response = f'> **{send}** - <@{str(user_id)}> \n\n{receive}'
        message_length = len(response)

        if message_length <= MAX_MESSAGE_LENGTH:
            await interaction.followup.send(response)
        else:
            number_of_messages = math.ceil(message_length / MAX_MESSAGE_LENGTH)
            starting_index = 0

            for current_message_num in range(1, number_of_messages + 1):
                if current_message_num == number_of_messages:
                    await interaction.followup.send(response[starting_index:])
                else:
                    last_space_index = response.rfind(" ", starting_index, MAX_MESSAGE_LENGTH * current_message_num)
                    await interaction.followup.send(response[starting_index:last_space_index])
                    starting_index = last_space_index + 1
        print(f"{user_id} sent: {send}, response: {receive}")
    except Exception as e:
        await interaction.followup.send('> **Error: Something went wrong, please try again later!**')
        print(f"Error while sending:{send} in chatgpt model, error: {e}")


async def send_timeout(interaction):
    embed = discord.Embed(colour=discord.Colour.from_str("#503b83"), description="**Mighty Pythian, kindly await the resolution of a previous Pythian's question. Your patience is appreciated, as the wisdom of Pythia shall soon illuminate your path. <a:pythfresh:1030876823137034413>**")
    embed.set_thumbnail(url="https://i.imgur.com/e87do2V.png")
    await interaction.followup.send(embed=embed)
