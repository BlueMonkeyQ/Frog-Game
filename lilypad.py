import item
from typing import List

class Crew():
    def __init__(self, name) -> None:
        self.name = name
        self.job = None
        self.tool: item.Item = None

    def setJob(self,job):
        self.job = job

    def setTool(self,tool: item.Item):
        self.tool = tool

    def setName(self,name):
        self.name = name

    def getTool(self):
        return self.tool

class Lilypad():
    def __init__ (self):

        self.storage: List[item.Item] = []
        self.storage_fish_max: int = 100
        self.storage_supplies_max: int = 100

        self.stove: bool = False
        self.tier: int = 1

        self.tools: List[item.Item] = []
        self.tools_max: int = 1

        self.crew: List[Crew] = []
        self.crew_max = 1
        
    # ---------- Crew ----------

    def crewAdd(self,crew: Crew):
        """"""
        if len(self.crew) == self.crew_max:
            return False
        else:
            self.crew.append(crew)
            return True

    # ---------- Tool ----------
    def toolSet(self, item:item.Item, slot:int):
        """"""
        
        if item.getType() != "tool":
            return False
        
        if len(self.tools) == 0:
            self.tools.append(item)
            self.storage.remove(item)
        else:
            current_tool = self.tools[slot]
            self.storage.remove(item)
            self.storage.append(current_tool)
            self.tools[slot] = item

        return True

    # ---------- Storage ----------
    def storageFindId(self,id):
        """Find Object given ID"""

        for i in self.storage:
            if i.getId() == id: return i
        return None
    
    def storageGetType(self,_type):
        """"""

        items: List[item.Item] = []
        
        for i in self.getStorage():
            if i.getType() == _type:
                items.append(i)

        return items

    def storageAdd(self,id,amount):
        """"""

        item_json = item.getItem(id)
        item_object = self.storageFindId(id)
        max = self.getMax(item_json['type'])
        
        if item_object != None:
            item_object.setAmount(amount, max)

        else:
            item_object = item.createItem(id)
            item_object.setAmount(amount, max)
            self.storage.append(item_object)

        return True
    
    def storageRemove(self,id,amount):
        """"""

        item_json = item.getItem(id)
        item_object = self.storageFindId(id)
        max = self.getMax(item_json['type'])

        if item_object is None:
            return False
        
        else:
            item_object.setAmount(-amount, max)
            if item_object.getAmount() == 0:
                self.storage.remove(item_object)

        return True
    
    def getStorage(self):
        return self.storage
    def getStorageFishMax(self):
        return self.storage_fish_max
    def getStorageSuppliesMax(self):
        return self.storage_supplies_max
    def getMax(self,_type):
        if _type == "fish":
            return self.getStorageFishMax()
        elif _type == "supplies":
            return self.getStorageSuppliesMax()
        elif _type == 'tool':
            return 1
        
    def getCrew(self):
        return self.crew
    
    def getStove(self):
        return self.stove
    def getTier(self):
        return self.tier
    def getTools(self):
        return self.tools