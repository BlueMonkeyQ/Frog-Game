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

item_dict = getJson()

class Item():
    def __init__(self, id, name, max_stack, amount=0, eat=False):
        self.id = id
        self.name = name
        self.max_stack = max_stack
        self.amount = amount
        self.eat = eat

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
    
    def getEar(self):
        return self.eat