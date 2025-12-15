import requests
from . import api
from .api import Craft
from .craftpopup import CraftPopup
from textual.widgets import DataTable
from config import cfg
from rich.text import Text

class DBColumn():
    def __init__(self, valuename: str, colname: str):
        self.valuename = valuename
        self.colname = colname

class ItemTable(DataTable):
    def __init__(self):
        super().__init__()
        self.invcolumns = [
            DBColumn("name", "Item Name"),
            DBColumn("size", "Amount in Inventory"),
            DBColumn("craftable", "Is Craftable")
        ]
        self.indexcol = "id"

        self.data = api.get("/api/items/inv")

        self.cursor_type = "row"
        self.sortmethod = "name"

    BINDINGS = [
        ("n", "sort_name", "Sort by Name"),
        ("a", "sort_size", "Sort by Amount"),
        ("c", "sort_craftable", "Sort by Craftable")
    ]

    def on_mount(self):
        for col in self.invcolumns:
            self.add_column(col.colname, key=col.valuename)
        
        for entry in self.data:
            row = []
            for col in self.invcolumns:
                cell = entry[col.valuename]
                row.append(cell)
            
            self.add_row(*row, key=entry[self.indexcol])
        
        self.sort("name")
    
    def action_sort_name(self):
        if self.sortmethod == "name":
            self.sort("name", reverse=True)
            self.sortmethod = "namereverse"
        else:
            self.sort("name")
            self.sortmethod = "name"
    
    def action_sort_size(self):
        if self.sortmethod == "size":
            self.sort("size", "name", reverse=True)
            self.sortmethod = "sizereverse"
        else:
            self.sort("size", "name")
            self.sortmethod = "size"
    
    def action_sort_craftable(self):
        if self.sortmethod == "craftable":
            self.sort("craftable", "name", reverse=True)
            self.sortmethod = "craftablereverse"
        else:
            self.sort("craftable", "name")
            self.sortmethod = "craftable"
    
    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        for row in self.data:
            if row["id"] == event.row_key:
                selectedrow = row
                break

        if selectedrow["craftable"] == True:
            craft = Craft(type="item", id=selectedrow["id"])
            self.mount(CraftPopup(craft=craft))