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
        "skill": None,
        "skills": {},
        "tool": None,
        "supply": None,
        "value": None,
        "amount": 0,
        "max": 1
    }

    json_data = getItem(id)

    for key, value in default_values.items():
        if key not in json_data:
            json_data[key] = value

    return Item(
        id=id,
        name=json_data["name"],
        _type=json_data["type"],
        skill=json_data["skill"],
        skills=json_data["skills"],
        tool=json_data["tool"],
        supply=json_data["supply"],
        value=json_data["value"],
        amount=json_data["amount"],
        max=json_data["max"]
    )

item_dict = getJson()

class Item:
    def __init__(self, id, name, _type, skill, skills, tool, supply, value, amount, max):
        self.id = id
        self.name = name
        self.type = _type
        self.skill = skill
        self.skills = skills
        self.tool = tool
        self.supply = supply
        self.value = value
        self.amount = amount
        self.max = max

    # ---------- Setters ----------
    def addAmount(self,amount):
        self.amount += amount

        if self.amount >= self.max:
            remainder = self.amount - self.max
            self.amount = self.max
            return remainder

        return 0
    
    def removeAmount(self,amount):
        self.amount -= amount
        if self.amount <= 0:
            self.amount = 0    
        return True


    def setAmount(self, amount):
        self.amount += amount

        if self.amount >= self.max:
            remainder = self.amount - self.max
            self.amount = self.max
            return remainder
        
        elif self.amount <= 0:
            self.amount = 0
        
        return self.amount

    # ---------- Getters ----------
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getSkill(self):
        return self.skill

    def getSkills(self):
        return self.skills

    def getTool(self):
        return self.tool
    
    def getSupply(self):
        return self.supply

    def getValue(self):
        return self.value

    def getAmount(self):
        return self.amount
    
    def getMax(self):
        return self.max
