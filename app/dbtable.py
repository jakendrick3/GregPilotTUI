from textual.widgets import DataTable
import requests

class DBColumn:
    def __init__(self, db: str, visible: str):
        self.db = db
        self.visible = visible

class DBTable(DataTable):
    def __init__(self, *, columns: list[DBColumn], endpoint: str):
        super().__init__()
        self.columnobjs = columns

        baseurl = "http://localhost:8000"
        url = baseurl + endpoint

        response = requests.get(url=url)
        self.data = response.json()

    def on_mount(self):
        for col in self.columnobjs:
            self.add_column(col.visible)
        
        for entry in self.data:
            row = []
            for col in self.columnobjs:
                row.append(entry[col.db])
            self.add_row(*row)