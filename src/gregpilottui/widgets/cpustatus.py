from gregpilottui import api
from textual.widgets import DataTable

class DBColumn():
    def __init__(self, valuename: str, colname: str):
        self.valuename = valuename
        self.colname = colname

class CPUTable(DataTable):
    def __init__(self):
        super().__init__(
            cursor_type = "row"
        )

        self.border_title = "Crafting CPUs"
        self.zebra_stripes = True

        self.invcolumns = [
            DBColumn("name", "Name"),
            DBColumn("busy", "Status"),
            DBColumn("coprocessors", "Coprocessors"),
            DBColumn("storage", "Storage (KB)")
        ]

        self.indexcol = "id"

    BINDINGS = [
        ("r", "refresh", "Refresh")
    ]

    async def on_mount(self):
        await self.action_refresh()

    async def action_refresh(self):
        self.clear(columns=True)
        self.data = await api.get("/api/cpus")

        for col in self.invcolumns:
            self.add_column(col.colname, key=col.valuename)
        
        for entry in self.data:
            row = []
            for col in self.invcolumns:
                cell = entry[col.valuename]

                if col.valuename == "busy":
                    if entry["busy"] == True:
                        cell = "Working"
                    else:
                        cell = "Idle"
                elif isinstance(cell, str):
                    cell = cell.capitalize()

                row.append(cell)
            
            self.add_row(*row, key=entry[self.indexcol])
        
        self.sort("name")