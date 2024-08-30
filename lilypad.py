import item
from typing import List

class Lilypad():
    def __init__ (self):

        self.storage: List[item.Item] = []
        self.storage_max: int = 10

        self.stove: bool = True
        self.tier: int = 1

    # ---------- Storage ----------
    def storageGetIndex(self,index):
        """Returns the item in the given index"""
        return self.storage[index]

    def storageFindId(self,id):
        """Find Object given ID"""
        items: List[item.Item] = []
        for i in self.storage:
            if i.getId() == id: 
                items.append(i)
        return items
    
    def storageGetType(self,_type):
        """"""

        items: List[item.Item] = []
        
        for i in self.getStorage():
            if i.getType() == _type:
                items.append(i)

        return items

    def storageAdd(self,id,amount):
        """"""
        items = self.storageFindId(id)
        item_object = None
        for i in items:
            if i.getAmount() != i.getMax():
                item_object = i
                break

        if item_object != None:
            amount = item_object.addAmount(amount)

        while True:
            if amount > 0:
                if len(self.storage) != self.storage_max:
                    item_object = item.createItem(id)
                    amount = item_object.addAmount(amount)
                    self.storage.append(item_object)
                else:
                    return amount
            else:
                break

        return 0
    
    def storageRemove(self,index,amount):
        """"""
        item_object = self.storage[index]

        if item_object is None:
            return False
        
        else:
            item_object.removeAmount(amount)
            if item_object.getAmount() == 0:
                self.storage.remove(item_object)

        return True
    
    # ---------- Getters ----------
    def getStorage(self):
        return self.storage  
    def getStorageMax(self):
        return self.storage_max    
    def getStove(self):
        return self.stove
    def getTier(self):
        return self.tier