from textual.widgets import DataTable
import requests

class DBTable(DataTable):
    def __init__(self, *, columns: list, url: str):
        super().__init__()
        self.listedcolumns = columns

        response = requests.get(url=url)
        self.data = response.json()

    def on_mount(self):
        self.add_columns(*self.listedcolumns)
        
        for entry in self.data:
            row = []
            for col in self.listedcolumns:
                row.append(entry[col])
            self.add_row(*row)