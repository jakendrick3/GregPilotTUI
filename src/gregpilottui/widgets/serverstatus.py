from gregpilottui import api
from textual.widgets import Label

class ServerStatus(Label): 
    async def on_mount(self):
        self.border_title = "Server Status"

        self.serverstatus = await api.get("/api/server")

        if self.serverstatus["online"] == True:
            self.content = "Online"
            self.add_class("serverup")
        else:
            self.add_class("serverdown")
            self.content = "Offline"