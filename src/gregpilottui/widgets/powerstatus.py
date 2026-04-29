from gregpilottui import api
from textual.widgets import Label, ProgressBar
from textual.containers import Vertical

class PowerStatus(Vertical): 
    async def on_mount(self):
        self.border_title = "Power Level"

        self.power = await api.get("/api/power")

        self.mount(ProgressBar(total=1, id="powerbar", show_eta=False),
            Label(f"{round(self.power["powerstored"] / 1000000, 2)}MEU / {round(self.power["powermax"] / 1000000, 2)}MEU", id="powerlabel")
        )

        self.query_one(ProgressBar).update(progress=(self.power["powerstored"] / self.power["powermax"]))