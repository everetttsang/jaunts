# import Jaunt
from app.Jaunt import Jaunt


class GoodMorning(Jaunt):
    gm_counter: int = 0
    game_id: str = "gm"

    def __init__(self, channel_id: int):
        super().__init__()
        self.gm_counter = 0
        self.channel_id = channel_id
        self.enabled = False

    def enable(self):
        self.enabled = True
        return f"Good Morning Counter enabled: {self.enabled}"

    def on_event(self, message) -> str or None:
        print(f"Message received. Contents.{message}")
        content = message.content
        author = message.author
        channel = message.channel

        if message.channel.id != self.channel_id:
            return
        if not self.enabled:
            return

        try:
            if 'gm' in content.lower():
                return self._format(
                    m=self._increment_count()
                )
            else:
                self._reset_count()
                return

        except Exception as e:
            print(e)

    def _increment_count(self) -> int:
        self.gm_counter = self.gm_counter + 1
        return self.gm_counter

    def _reset_count(self) -> None:
        self.gm_counter = 0

    def _format(self, m: int) -> str:
        return f"`gm streak: {m}`" + self._fire(count=m)

    @staticmethod
    def _fire(count: int) -> str:
        r = "\n"
        for x in range(0, int(count / 5)):
            if len(r) > 1985:
                break
            r = r + ":fire::fire::fire::fire::fire:\n"
        return r
