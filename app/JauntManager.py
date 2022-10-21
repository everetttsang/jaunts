from app.GoodMorning import GoodMorning
import json


class JauntManager:
    good_morning: GoodMorning
    status: dict

    def __init__(self):
        self.good_morning = GoodMorning()
        self.status = {
            self.good_morning.game_id: False
        }

    def toggle_game(self, game: str):
        stat = {
            True: "Enabled",
            False: "Disabled"
        }
        status = self.status.get(game)
        update_dict = {
            game: not status
        }
        if game == 'gm':
            self.status.update(update_dict)
            return f"{game}: {stat.get(self.status.get(game))}."
        return f"Could not enable {game}."

    def get_status(self, game: str = None) -> str or None:
        if not game:
            return False
        else:
            return self.status.get(game, f"All jaunts are currently disabled.")

    def tickle_games(self, message=None):
        if self.get_status("gm"):
            return self.good_morning.on_event(message=message)
