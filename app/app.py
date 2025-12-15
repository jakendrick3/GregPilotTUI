from typing import Iterable
from textual.app import App, ComposeResult, SystemCommand
from textual.screen import Screen
from textual.widgets import Footer, Header, TabbedContent, TabPane, Markdown
from .invtable import DBColumn, ItemTable

class GregPilotTUI(App):
    def get_system_commands(self, screen: Screen) -> Iterable[SystemCommand]:
        yield from super().get_system_commands(screen)  

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        
        with TabbedContent():
            with TabPane("Overview", id="overview"):
                pass
            with TabPane("Items", id="items"):
                yield ItemTable()
            #with TabPane("Fluids", id="fluids"):
            #    yield InventoryTable(endpoint="/api/fluids/inv", invcolumns=[DBColumn("name", "Fluid Name"), DBColumn("amount", "Amount (L)")])
            #with TabPane("Essentia", id="essentia"):
            #    yield InventoryTable(endpoint="/api/essentia/inv", invcolumns=[DBColumn("name", "Essentia"), DBColumn("amount", "Amount")])