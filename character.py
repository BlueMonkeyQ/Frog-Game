import item
from typing import List

class Character():
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name
    
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
    
class Player(Character):
    def __init__(self, name="Frog", location={}, log={}):
        super().__init__(name)
        self.gold = 0
        self.fishing_xp = 0
        self.cooking_xp = 0
        self.tool: item.Item = None
        self.location: dict = location
        self.log: dict = log

    def getGold(self):
        return self.gold

    def getFishingXp(self):
        return self.fishing_xp

    def getCookingXp(self):
        return self.cooking_xp
    
    def getTool(self):
        return self.tool
    
    def getLocation(self):
        return self.location
    
    def setGold(self,gold):
        self.gold += gold
        if self.gold < 0:
            self.gold = 0
    
    def setFishingXp(self,xp):
        self.fishing_xp += xp

    def setCookingXp(self,xp):
        self.cooking_xp += xp

    def setTool(self,tool:item.Item):
        if self.tool is None:
            self.tool = tool
        else:
            old_tool = self.tool
            self.tool = tool
            return old_tool

    def setLocation(self,location):
        self.location = location

    def setLogSkill(self,skill,thing,key,value):
        self.log['skills'][skill][thing][key] += value