import random
import math
import json
from pathlib import Path

def skillCheck(player_lvl: int, object_lvl: int):
    """Checks if player skill lvl is >= Object lvl"""
    if player_lvl >= object_lvl:
        return True
    else:
        return False
    
def rollChance(min:int, max: int):
    """Returns the roll between a min and max number"""
    return random.randint(min,max)

def getDrops(drop_table):
    """Goes through each drop in a drop table and returns drops"""
    
    drops = []
    for drop in drop_table:
        id = drop[0]
        chance = drop[1]
        min_amount = drop[2]
        max_amount = drop[3]

        if rollChance(1,100) <= chance:
            amount = random.randint(min_amount, max_amount)
            drops.append([id,amount])
    return drops

def getXP(xp:int, cut:float):
    """Returns the amount of xp given"""
    return math.ceil(xp*cut)

def getJSONSkills(skill):
    with open (Path(f"data/skills/{skill}.json")) as f:
        json_data = f.read()
    return json.loads(json_data)

