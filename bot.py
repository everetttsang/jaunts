import os

import discord
from discord import Intents
from dotenv import load_dotenv
from app import JauntManager
from app.JauntManager import  JauntManager
from commands import Command


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

eh = discord.Client(intents=Intents.default())


class HoleClient(discord.Client):
    message: discord.Message
    manager: JauntManager

    def __init__(self):
        intents = Intents.default()
        setattr(intents, 'message_content', True)
        setattr(intents, 'messages', True)
        self.gm_counter = 0
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

        # Initialize Games
        self.manager = JauntManager()

        print(f"Games loaded.\n Status:\n {self.manager.get_status()}")
        pass

    async def on_message(self, message):
        # bot cannot react to itself
        if message.author.id == self.user.id:
            return
        cmd = Command(context=self.manager, message=message)

        res = cmd.process_event(message)
        if res:
            await self.get_channel(message.channel.id) \
                .send(self.blockify(res))

    @staticmethod
    def blockify(message: str) -> str:
        return message if '`' in message else f"`{message}`"

client = HoleClient()
client.run(token=TOKEN)
