from .dbtable import DBColumn

datastruct = {
    'ii': {
        'tabname': "Item Inventory",
        'endpoint': "/items/log",
        'columns': [
            DBColumn("id", "Item ID"),
            DBColumn("size", "Item Amount")
        ]
    },
    'fi': {
        'tabname': "Fluid Inventory",
        'endpoint': "/fluids/log",
        'columns': [
            DBColumn("id", "Fluid ID"), 
            DBColumn("amount", "Fluid Amount (L)")
        ]
    },
    'it': {
        'tabname': "Items",
        'endpoint': "/items",
        'columns': [
            DBColumn("id", "Item ID"), 
            DBColumn("name", "Item Name")
        ]
    },
    'fl': {
        'tabname': "Fluids",
        'endpoint': "/fluids",
        'columns': [
            DBColumn("id", "Fluid ID"), 
            DBColumn("name", "Fluid Name")
        ]
    }
}