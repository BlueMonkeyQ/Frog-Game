import json
from pathlib import Path


def getJson():
    with open(Path(f"data/items/items.json")) as f:
        json_data = f.read()
    return json.loads(json_data)


def getItem(id) -> dict:
    """Returns item object given id"""
    return item_dict[str(id)]


def getItemName(id):
    """Returns the name of the item given the ID"""
    return item_dict[str(id)]["name"]


def getItemValue(id):
    "Returns the value of the item given the ID"
    return item_dict[str(id)]["value"]


def createItem(id):
    default_values = {
        "type": None,
        "skills": {},
        "tool": None,
        "value": None,
        "amount": 0
    }

    json_data = getItem(id)

    for key, value in default_values.items():
        if key not in json_data:
            json_data[key] = value

    return Item(
        id=id,
        name=json_data["name"],
        _type=json_data["type"],
        skills=json_data["skills"],
        tool=json_data["tool"],
        value=json_data["value"],
        amount=json_data["amount"],
    )

item_dict = getJson()


class Item:
    def __init__(self, id, name, _type, skills, tool, value, amount):
        self.id = id
        self.name = name
        self.type = _type
        self.skills = skills
        self.tool = tool
        self.value = value
        self.amount = amount

    # ---------- Setters ----------
    def setAmount(self, amount, max):
        self.amount += amount
        if self.amount >= max:
            self.amount = max
        elif self.amount <= 0:
            self.amount = 0
        return True

    # ---------- Getters ----------
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getSkills(self):
        return self.skills

    def getTool(self):
        return self.tool

    def getValue(self):
        return self.value

    def getAmount(self):
        return self.amount
