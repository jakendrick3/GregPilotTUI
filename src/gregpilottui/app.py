from os import makedirs, path
from typing import Iterable
from textual import work
from textual.app import App, ComposeResult, SystemCommand
from textual.screen import Screen
from textual.widgets import Footer, Header, TabbedContent, TabPane, Placeholder
from textual.containers import Container
from textual.lazy import Lazy
from platformdirs import user_config_dir
from gregpilottui.widgets.invtable import ItemTable, FluidTable, EssentiaTable
from gregpilottui.widgets.serverstatus import ServerStatus
from gregpilottui.screens.initpopup import InitialConfigScreen
from gregpilottui.config import get_config, reload_config
from pathlib import Path

class PrimaryScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        
        with TabbedContent():
            with TabPane("Overview", id="overview"):
                yield Container(
                    Placeholder("Rules", id="rules", classes="maininfo"),
                    ServerStatus(classes="maininfo"),
                    Placeholder("Crafting Requests", id="requests", classes="maininfo"),
                    Placeholder("Favorites", id="favorites", classes="maininfo"),
                    Placeholder("Power", id="power", classes="maininfo"),
                    id="mainpage"
                ) 
            with TabPane("Items", id="items"):
                yield Lazy(ItemTable())
            with TabPane("Fluids", id="fluids"):
                yield Lazy(FluidTable())
            with TabPane("Essentia", id="essentia"):
                yield Lazy(EssentiaTable())

class GregPilotTUI(App):
    CSS_PATH = "gp.tcss"

    def __init__(self):
        super().__init__()

    MODES = {
        "PrimaryMode": PrimaryScreen
    }

    DEFAULT_MODE = "PrimaryMode"

    @work
    async def on_mount(self):
        cfgdir = user_config_dir(appname = "GregPilotTUI")
        if not path.exists(cfgdir):
            makedirs(user_config_dir(appname = "GregPilotTUI"))
            
        config = get_config()
        
        if config.sections() == []:
            baseurl = await self.push_screen_wait(InitialConfigScreen())
            config["DEFAULT"] = {}
            config["API"] = {}
            config["API"]["baseurl"] = baseurl
            cfgfile = Path(user_config_dir("GregPilotTUI")) / "config.ini"
            
            with open(cfgfile, "w") as f:
                config.write(f)
                reload_config()
        
            self.switch_mode("PrimaryMode")

    def get_system_commands(self, screen: Screen) -> Iterable[SystemCommand]:
        yield from super().get_system_commands(screen)