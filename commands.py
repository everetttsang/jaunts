
from app.JauntManager import JauntManager

class Command:
    context: JauntManager
    payload: str

    def __init__(self, context, message):
        self.payload = message
        self.context = context

    def process_event(self, message):
        content = message.content
        channel = message.channel
        try:
            command = content.split()
            instruction_word = command[0]
        except Exception as e:
            return

        if instruction_word != '.jaunt':
            return self.context.tickle_games(message=message)

        try:
            if command[1] == 'toggle':
                if command[2] == 'gm':
                    return self.context.toggle_game(game='gm')

        except IndexError as e:
            return f"Jaunt Failed: {e}"
        except Exception as e:
            return
        return

    @staticmethod
    def trigger_jaunt(message):
        return