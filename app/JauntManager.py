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
            if cls.get_status(game=game,
                              message=message) is not None:
                gm = cls.get_game(game=game,
                                  message=message)
            else:
                gm = GoodMorning(channel_id=message.channel.id)
            r = gm.enable()
            cls.games[game].append(gm)
            return r

    @classmethod
    def end_game(cls, message, game_key: str):
        if game_key == 'gm':
            for game in cls.games[game_key]:
                if game.channel_id == message.channel.id and game.enabled:
                    return game.disable()
                else:
                    return "Game is already disabled."

    @classmethod
    def game_exists(cls, message, game: str):
        if game == 'gm':
            for game in cls.games[game]:
                if game.channel_id == message.channel.id:
                    return True
        return False

    @classmethod
    def toggle_game(cls, message, game: str):
        stat = {
            True: "Enabled",
            False: "Disabled"
        }
        status = cls.get_status(message=message,
                                game=game)
        update_dict = {
            game: not status
        }
        exists = cls.game_exists(message=message,
                                 game=game)
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
            return cls.start_game(message=message,
                                  game=game) if update_dict[game] else cls.end_game(message=message,
                                                                                    game_key=game)
        return f"Could not enable {game}."
        pass

    @classmethod
    def get_status(cls, game: str, message) -> str or None:
        for jaunt in cls.games[game]:
            if jaunt.channel_id == message.channel.id:
                return jaunt.enabled
        return

    @classmethod
    def get_game(cls, game: str, message) -> str or None:
        for jaunt in cls.games[game]:
            if jaunt.channel_id == message.channel.id:
                return jaunt
        return

    @classmethod
    def trigger_games(cls, message=None):
        for game in cls.games['gm']:
            if game.enabled:
                return game.on_event(message=message)
