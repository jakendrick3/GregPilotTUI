from typing import Iterable
from textual.app import App, ComposeResult, SystemCommand
from textual.screen import Screen
from textual.widgets import Footer, Header, TabbedContent, TabPane, Markdown
from .dbtable import DBTable, DBColumn
from .api import datastruct

class GregPilotTUI(App):
    def get_system_commands(self, screen: Screen) -> Iterable[SystemCommand]:
        yield from super().get_system_commands(screen)  

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        
        with TabbedContent():
            with TabPane("Overview", id="ov"):
                pass
            
            tabs = ["ii", "fi", "it", "fl"]

            for tab in tabs:
                with TabPane(datastruct[tab]["tabname"], id=tab):
                    yield DBTable(columns=datastruct[tab]["columns"], endpoint=datastruct[tab]["endpoint"])