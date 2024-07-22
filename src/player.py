from item import *
from typing import List

class Player():
    def __init__(self):
        # Skills
        self.fishing_xp = 0
        # General
        self.name = "Frog"
        self.gold = 0
        self.inventory: List[Item] = [] # List of item Objects
        self.inventory_max = 1 # Inventory Size

    def displayStats(self):
        print(f"---------- General ----------")
        print(f":: {self.name}")
        print(f":: ${self.gold}")
        print(f"----- Skills -----")
        print(f":: Fishing Lvl: {self.getLevel(self.fishing_xp)} XP: {self.fishing_xp}")
        print(f"----- Skills -----")
        print(f"----- Inventory --")
        for i in self.inventory:
            print(f":: #{i.getAmount():<2} {i.getName()}")
        print(f"----- Inventory --")
        print("---------- General ----------")

    def getLevel(self, xp):
        level = 1
        next_level = 2
        while True:
            xp_needed = int(((next_level-1)+(300*2)*((next_level-1)/7)))
            if xp >= xp_needed:
                level += 1
                next_level += 1
            else:
                break
        return level
    
    # ---------- Inventory ----------
    def displayInventory(self):
        print(f":: -- Inventory --")
        for i in self.inventory:
            print(f":: #{i.getAmount():<2} {i.getName()}")
        print(f":: -- --")

    def inventoryAdd(self,id,amount):
        """
        Adds items into the players inventory
        If the item exist in the inventory, then add to total amount
        elif item exist but max stack is reached, then create new object
        else create new object
        """
        item_object = item_dict[f"{id}"]

        item = None
        for i in self.inventory:
            if i.getId() == id and (i.getAmount() < i.getMaxStack()):
                item = i
                
        if item:
            amount = item.setAmount(amount)

        while True:
            if amount == 0:
                break

            elif len(self.inventory) < self.inventory_max and amount != 0:
                item = Item(id=id,
                                name=item_object['name'],
                                max_stack=item_object['max_stack'])
                amount = item.setAmount(amount)
                self.inventory.append(item)

            elif len(self.inventory) == self.inventory_max:
                print(f" Inventory full... Dropping #{amount} {item_object['name']}")
                break

            else:
                break

    def inventoryRemove(self,id,amount):
        """
        Removes Item and amount from players inventory
        If the amount > 0 keep item
        else, remove item from inventory
        """

        item = None
        for i in self.inventory:
            if i.getId() == id:
                item = i
                break
        item.setAmount(-amount)
        if i.getAmount() == 0:
            self.inventory.remove(item)
                    
    # ---------- Setters ----------
    def setFishingXp(self,xp):
        print(f"{xp} Fishing xp")
        self.fishing_xp += xp

    # ---------- Getters ----------
    def getFishingXp(self):
        return self.fishing_xp
    
    def getInventory(self):
        return self.inventory