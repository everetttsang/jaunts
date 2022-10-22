
from app.JauntManager import JauntManager


class Command:
    context: JauntManager
    payload: str
    record: dict

    @classmethod
    def process_event(cls, message, manager):
        content = message.content
        channel = message.channel
        try:
            command = content.split()
            instruction_word = command[0]
        except Exception as e:
            return

        if instruction_word != '.jaunt':
            return manager.trigger_games(message=message)

        try:
            if command[1] == 'toggle':
                if command[2] == 'gm':
                    # if message.author.id in self.record[str(message.guild.id)]['admins']:
                    return manager.toggle_game(message=message,
                                               game='gm')

        except IndexError as e:
            return f"Jaunt Failed: {e}"
        except Exception as e:
            return
        return
