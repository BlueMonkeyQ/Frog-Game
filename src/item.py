import json
from pathlib import Path

def getJson():
    with open (Path(f"data/items/items.json")) as f:
        json_data = f.read()
    return json.loads(json_data)

def getItem(id) -> dict:
    """Returns item object given id"""
    return item_dict[f"{id}"]

def getItemName(id):
    """Returns the name of the item given the ID"""
    return item_dict[f"{id}"]["name"]

def getItemValue(id):
    "Returns the value of the item given the ID"
    return item_dict[f"{id}"]['value']

def itemFromJson(json_data, id):
    default_values = {
        'amount': 0,
        'max_stack': 1,
        'eat': False,
        'backpack': None,
        'tool': None
    }

    for key, value in default_values.items():
        if key not in json_data:
            json_data[key] = value

    return Item(
        id=id,
        name=json_data['name'],
        max_stack=json_data['max_stack'],
        amount=json_data['amount'],
        eat=json_data['eat'],
        tool=json_data['tool'],
        backpack=json_data['backpack']
    )

item_dict = getJson()

class Item():
    def __init__(self, id, name, max_stack, amount, eat, tool, backpack):
        self.id = id
        self.name = name
        self.max_stack = max_stack
        self.amount = amount
        self.eat = eat
        self.tool = tool
        self.backpack = backpack

    # ---------- Setters ----------
    def setAmount(self,amount):
        self.amount += amount
        if self.amount > self.max_stack:
            remainder = self.amount - self.max_stack
            self.amount = self.max_stack
            return remainder
        elif self.amount <= 0:
            self.amount = 0
        return 0

    # ---------- Getters ----------
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getMaxStack(self):
        return self.max_stack

    def getAmount(self):
        return self.amount
    
    def getEat(self):
        return self.eat
        
    def getTool(self):
        return self.tool
        
    def getBackpack(self):
        return self.backpack
    
    def getBackpackCapacity(self):
        return self.backpack['capacity']