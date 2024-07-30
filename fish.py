import json
from pathlib import Path

def getJson():
    with open(Path(f"data/items/fish.json")) as f:
        json_data = f.read()
    return json.loads(json_data)

def getFish(id) -> dict:
    """Returns item object given id"""
    return fish_dict[f"{id}"]

def itemFromJson(id):
    fish = getFish(id)

    return Fish(
        id=id,
        name=fish["name"],
        lvl=fish["lvl"],
        _type=fish["type"],
        value=fish["value"],
    )
fish_dict = getJson()

class Fish:
    def __init__(self, id, name, lvl, _type, value):
        self.id = id
        self.name = name
        self.lvl = lvl
        self._type = _type
        self.value = value

    # ---------- Setters ----------
    def setAmount(self, _amount):
        self.amount = _amount

    # ---------- Getters ----------
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getLvl(self):
        return self.lvl

    def getType(self):
        return self._type

    def getValue(self):
        return self.value
