from typing import Iterable
from textual.app import App, ComposeResult, SystemCommand
from textual.screen import Screen
from textual.widgets import Footer, Header, Tabs
from .dbtable import DBTable

class GregPilotTUI(App):
    def get_system_commands(self, screen: Screen) -> Iterable[SystemCommand]:
        yield from super().get_system_commands(screen)  

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        columns = ["id", "rawdamage", "rawid", "name"]
        url = "http://localhost:8000/items"
        yield DBTable(columns=columns, url=url)
        #yield Tabs("Overview", "Item Inventory", "Fluid Inventory", "Items", "Fluids")

