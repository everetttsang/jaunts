import os

import discord
from discord import Intents
from dotenv import load_dotenv
from app import JauntManager
from app.JauntManager import JauntManager
from commands import Command
from config import CLUSTER_PATH
import json
from typing import List

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class HoleClient(discord.Client):
    message: discord.Message
    manager: JauntManager
    record: dict

    def __init__(self):
        intents = Intents.default()
        setattr(intents, 'message_content', True)
        setattr(intents, 'messages', True)
        setattr(intents, 'members', True)
        self.gm_counter = 0
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        doc = dict()
        # Initialize Games
        self.manager = JauntManager()
        guilds = self.guilds
        for guild in guilds:
            admins: List[int or None] = list()

            for member in guild.members:
                try:
                    if member.guild_permissions.administrator:
                        admins.append(member.id)
                except Exception:
                    pass

        print(f"Games loaded.\n Status:\n {self.manager.get_status()}")
        pass

    async def on_message(self, message):
        # bot cannot react to itself
        if message.author.id == self.user.id:
            return

        print(f"\n Author ID{message.author.id}, User_ID {self.user.id}")
        print(message.content)

        res = Command.process_event(message=message,
                                    manager=self.manager)
        if res:
            await self.get_channel(message.channel.id) \
                .send(self.blockify(res))

    @staticmethod
    def blockify(message: str) -> str:
        return message if '`' in message else f"`{message}`"

    @classmethod
    def update_record(cls, doc):
        cls.record = doc


client = HoleClient()
client.run(token=TOKEN)
