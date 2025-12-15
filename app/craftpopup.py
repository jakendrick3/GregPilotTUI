from textual.widgets import Input
from .api import Craft

class CraftPopup(Input):
    def __init__(self, *, craft: Craft):
        super().__init__()
        self.craft = craft
        self.type = "integer"
        self.placeholder = "Enter amount to craft..."
    
    def on_mount(self):
        pass

    async def on_input_submitted(self, event: Input.Submitted):
        self.craft.amount = int(event.value)
        self.craft.submit()
        self.remove()