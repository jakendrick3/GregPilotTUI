from gregpilottui import api
from datetime import datetime, timezone
from textual.widgets import DataTable

class DBColumn():
    def __init__(self, valuename: str, colname: str):
        self.valuename = valuename
        self.colname = colname

class CraftRequestsTable(DataTable):
    def __init__(self):
        super().__init__(
            cursor_type = "row"
        )

        self.border_title = "Craft Requests"

        self.invcolumns = [
            DBColumn("status", "Status"),
            DBColumn("id", "Name"),
            DBColumn("type", "Type"),
            DBColumn("amount", "Amount"),
            DBColumn("entered", "At")
        ]

        self.indexcol = "requestid"

    BINDINGS = [
        ("r", "refresh", "Refresh")
    ]

    async def on_mount(self):
        await self.action_refresh()

    async def action_refresh(self):
        self.clear(columns=True)
        self.data = await api.get("/api/requests/craft")

        for col in self.invcolumns:
            self.add_column(col.colname, key=col.valuename)
        
        for entry in self.data:
            row = []
            for col in self.invcolumns:
                cell = entry[col.valuename]

                if col.valuename == "entered":
                    cell = datetime.strptime(cell, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
                    cell = datetime.strftime(cell, "%m/%d %H:%M")
                elif col.valuename == "id":
                    try: 
                        getname = await api.get(f"/api/{entry["type"]}s", params={"id": entry["id"]})
                        cell = getname[0]["name"]
                    except:
                        cell = entry["id"]
                elif col.valuename == "amount":
                    if entry["type"] == "fluid":
                        cell = str(cell) + "ml"
                elif isinstance(cell, str):
                    cell = cell.capitalize()

                row.append(cell)
            
            self.add_row(*row, key=entry[self.indexcol])
        
        self.sort("entered", reverse=True)