import discord.client as Client
import discord.message as Message


class Jaunt:
    enabled: bool
    game_id: str

    def __init__(self):
        self.enabled = False

    async def on_event(self, message: Message):
        return
