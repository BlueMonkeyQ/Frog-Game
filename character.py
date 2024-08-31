import item
from rich import print
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
        self.woodcutting_xp = 0
        self.cooking_xp = 0
        self.tool_belt: List[item.Item] = []
        self.location: dict = location
        self.log: dict = log

    def getGold(self):
        return self.gold

    def getFishingXp(self):
        return self.fishing_xp
    
    def getWoodcuttingXp(self):
        return self.woodcutting_xp

    def getCookingXp(self):
        return self.cooking_xp
    
    def getToolBelt(self):
        return self.tool_belt

    def getToolBeltType(self,_type):
        for tool in self.tool_belt:
            if tool.type == _type:
                return tool
        return None
    
    def getToolBeltSkill(self,skill):
        tools = [tool.getName() for tool in self.tool_belt if skill in tool.getSkill()]
        return tools
    
    def getLocation(self):
        return self.location
    
    def setGold(self,gold):
        self.gold += gold
        if self.gold < 0:
            self.gold = 0
    
    def setFishingXp(self,xp):
        self.fishing_xp += xp

    def setWoodcuttingXp(self,xp):
        self.woodcutting_xp += xp

    def setCookingXp(self,xp):
        self.cooking_xp += xp

    def setLocation(self,location):
        self.location = location

    def setLogSkill(self,skill,thing,key,value):
        self.log['skills'][skill][thing][key] += value

    def setToolBelt(self,tool:item.Item):
        """
        If Tool type exist in belt, return old tool to inventory, then replace.
        Else, append tool to belt.
        """

        if tool.getType() != "tool":
            print.warning("Item is not a tool.")
            return False
        
        tool_type = tool.getTool()

        index = None
        for i in range(len(self.tool_belt)):
            if self.tool_belt[i].getTool() == tool_type:
                index = i
                break
        
        if index is not None:
            old_tool = self.tool_belt[index]
            self.tool_belt[index] = tool
            return old_tool
        else:
            self.tool_belt.append(tool)
            return None