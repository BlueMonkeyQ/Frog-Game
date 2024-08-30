from item import *
from typing import List

class Player:
    def __init__(self):
        # Skills
        self.fishing_xp = 0

        # General
        self.name = "Frog"
        self.gold = 0
        self.inventory: List[Item] = []  # List of item Objects
        self.inventory_max = 28  # Inventory Size
        self.tool_belt: Item = None
        self.bank: List[Item] = []  # List of item Objects with infinite stack size
        
        with open(Path(f"data/log/log.json")) as f:
            json_data = f.read()
        self.log: dict = json.loads(json_data) # Dictionary if stats

        # Equipment
        self.backpack: Item = None
        self.tool: Item = None

        # Location
        self.world = 'earth'
        self.location = 1

    def displayStats(self):
        print(f"---------- General ----------")
        print(f":: {self.name}")
        print(f":: ${self.gold}")
        print(f"----- Skills -----")
        print(f":: Fishing Lvl: {self.getLevel(self.fishing_xp)} XP: {self.fishing_xp}")
        print(f"----- Skills -----")
        print(f"----- Inventory {len(self.inventory)}/{self.inventory_max} -----")
        for i in self.inventory:
            print(f":: #{i.getAmount():<2} {i.getName()}")
        print(f"----- Inventory {len(self.inventory)}/{self.inventory_max} -----")
        print(f"----- Equipment -----")
        print(
            f":: Tool:     {self.tool.getName() if self.tool is not None else 'Empty'}"
        )
        print(
            f":: Backpack: {self.backpack.getName() if self.backpack is not None else 'Empty'}"
        )
        print(f"----- Equipment -----")
        print("---------- General ----------")

    def getLevel(self, xp):
        level = 1
        next_level = 2
        while True:
            xp_needed = int(((next_level - 1) + (300 * 2) * ((next_level - 1) / 7)))
            if xp >= xp_needed:
                level += 1
                next_level += 1
            else:
                break
        return level

    # ---------- Equipment ----------
    def equipEquipment(self, item: Item):
        """
        Equip Tool from inventory
        If tool exist in slot, add it back into inventory
        """
        try:
            current_equipped = None

            if item.getTool() is not None:
                if self.tool != None:
                    current_equipped = self.tool

                self.tool = item

            elif item.getBackpack() is not None:

                if (
                    self.backpack != None
                    and len(self.inventory) > item.getBackpackCapacity()
                ):
                    print(
                        f"{len(self.inventory) - item.getBackpackCapacity()} items overweight. Un-able to unequip current backpack"
                    )
                    return False

                else:
                    current_equipped = self.backpack

                self.backpack = item
                self.inventory_max = item.getBackpackCapacity()

            else:
                return False

            self.inventoryRemove(item.getId())
            if current_equipped:
                self.inventoryAdd(current_equipped.getId(), 1)
            return True

        except Exception as e:
            print(e)
            return False

    # ---------- Inventory ----------
    def displayInventory(self):
        print(f":: -- Inventory --")
        for i in self.inventory:
            print(f":: #{i.getAmount():<2} {i.getName()}")
        print(f":: -- --")

    def inventoryFindItem(self, id):
        """Returns item given id"""
        for i in self.inventory:
            if i.getId() == id:
                return i
        return None

    def inventoryGetItem(self, index):
        """Returns the item object from inventory"""
        return self.inventory[index]

    def inventoryAdd(self, id, amount):
        """
        Adds items into the players inventory
        If the item exist in the inventory, then add to total amount
        elif item exist but max stack is reached, then create new object
        else create new object
        """
        item_json = item_dict[f"{id}"]
        item_object = self.inventoryFindItem(id)

        if item_object != None:
            amount = item_object.calculateAmount(amount)

        while True:
            if amount == 0:
                break

            elif len(self.inventory) < self.inventory_max and amount != 0:
                item_object = itemFromJson(item_json, id)
                amount = item_object.calculateAmount(amount)
                self.inventory.append(item_object)

            elif len(self.inventory) == self.inventory_max:
                print("Inventory full")
                break

            else:
                break

        return amount

    def inventoryRemove(self, id, amount=1):
        """
        Removes Item and amount from players inventory
        If the amount > 0 keep item
        else, remove item from inventory
        """
        try:
            item_object = self.inventoryFindItem(id)

            if item_object is None:
                return False

            else:
                item_object.calculateAmount(-amount)
                if item_object.getAmount() <= 0:
                    self.inventory.remove(item_object)

            return True

        except Exception as e:
            print(e)
            return False

    def inventoryToBank(self, id, amount):
        """
        Removes item and amount from inventory to bank
        If item.amount <= 0 then remove item
        Else keep remaining amount
        """
        try:
            item_object = self.inventoryFindItem(id)

            if item_object is None:
                return False

            if amount > item_object.getAmount():
                amount = item_object.getAmount()

            self.bankAdd(id, amount)
            self.inventoryRemove(id, amount)

            return True

        except Exception as e:
            print(e)
            return False

    # # ---------- Bank ----------

    # def bankFindItem(self, id):
    #     """Returns index given id"""
    #     for i in self.bank:
    #         if i.getId() == id:
    #             return i
    #     return None

    # def bankAdd(self, id, amount):
    #     """
    #     Adds item into players bank
    #     If item exist in bank, just add to the amount count
    #     Else, create new item entry
    #     """
    #     try:
    #         item_object = self.bankFindItem(id)

    #         if item_object is None:
    #             item = itemFromJson(item_dict[f"{id}"], id)
    #             item.calculateAmount(amount, True)
    #             self.bank.append(item)

    #         else:
    #             item_object.calculateAmount(amount, True)

    #         return True

    #     except Exception as e:
    #         print(e)
    #         return False

    # def bankRemove(self, id, amount=1):
    #     """
    #     Removes item from bank
    #     If item.amount > 0 Keep item in banbk
    #     Else remove it
    #     """
    #     try:
    #         item_object = self.bankFindItem(id)

    #         if item_object is None:
    #             return False

    #         else:
    #             item_object.calculateAmount(-amount, True)
    #             if item_object.getAmount() <= 0:
    #                 self.bank.remove(item_object)

    #         return True

    #     except Exception as e:
    #         print(e)
    #         return False

    # def bankToInventory(self, id, amount):
    #     """
    #     Removes item and amount from bank to inventory
    #     If len(inventory) == inventory_max return False
    #     elif amount > item.max_stack return max_stack
    #     elif return amount
    #     if item.amount == 0 remove item from bank
    #     else keep
    #     """
    #     try:
    #         if len(self.inventory) == self.inventory_max:
    #             print("Inventory is at max capacity")
    #             return False

    #         item_object = self.bankFindItem(id)
    #         if amount > item_object.getAmount():
    #             amount = item_object.getAmount()

    #         new_amount = self.inventoryAdd(id, amount)

    #         if new_amount != 0:
    #             amount -= new_amount

    #         item_object.calculateAmount(-amount, True)

    #         if item_object.getAmount() == 0:
    #             self.bankRemove(id)

    #         return True

    #     except Exception as e:
    #         print(e)
    #         return False

    # ---------- Setters ----------
    def setFishingXp(self, xp):
        print(f"{xp} Fishing xp")
        self.fishing_xp += xp

    def setGold(self, _gold):
        print(f"{_gold} Gold")
        self.gold += _gold

    def setLogGold(self,key,value):
        self.log['gold'][key] += value

    def setLogSkill(self,skill,_type, key,value):
        self.log['skills'][skill][_type][key] += value

    # ---------- Getters ----------
    def getFishingXp(self):
        return self.fishing_xp

    def getInventory(self):
        return self.inventory

    def getInventoryMax(self):
        return self.inventory_max

    def getTool(self):
        return self.tool

    def getBackpack(self):
        return self.backpack

    def getGold(self):
        return self.gold

    def getLog(self):
        return self.log
    
    def getWorld(self):
        return self.world
    def getLocation(self):
        return self.location