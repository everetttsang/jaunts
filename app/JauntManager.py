from app.GoodMorning import GoodMorning


class JauntManager:
    good_morning: GoodMorning
    status: dict
    games: dict

    status = {
        str(GoodMorning.game_id): False

    }
    games = {
        str(GoodMorning.game_id): list()
    }

    @classmethod
    def start_game(cls, message, game: str):
        if game == 'gm':
            gm = GoodMorning(channel_id=message.channel.id)
            gm.enable()
            cls.games[game].append(gm)
            return "Game enabled."

    @classmethod
    def toggle_game(cls, message, game: str):
        stat = {
            True: "Enabled",
            False: "Disabled"
        }
        status = cls.status.get(game)
        update_dict = {
            game: not status
        }
        print(f"Toggling")

        # if not update_dict[game]:
        #     # reset game
        #     return
        # else:
        #     # put game record w/ channel id in the record
        #     rec = {
        #         str(message.channel.id): dict(
        #             most_recent_poster=message.author.id,
        #             game_data={"gm_counter": 0}
        #         )
        #     }
        #     file = dict()
        #     record = record.get(str(message.guild)).get('jaunts')

        if game == 'gm':
            cls.status.update(update_dict)
            return f"{game}: {stat.get(cls.status.get(game))}."
        return f"Could not enable {game}."
        pass

    @classmethod
    def get_status(cls, game: str = None) -> str or None:
        if not game:
            return False
        else:
            return cls.status.get(game, f"All jaunts are currently disabled.")

    @classmethod
    def trigger_games(cls, message=None):
        for game in cls.games['gm']:
            if game.enabled:
                return game.on_event(message=message)
