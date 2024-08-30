import item
import json
import random
import math
from lilypad import Lilypad
from character import Player
from pathlib import Path

def getJson(skill):
    with open(Path(f"data/skills/{skill}.json")) as f:
        json_data = f.read()
    return json.loads(json_data)

def rollChance(min: int, max: int):
    """Returns the roll between a min and max number"""
    if min < 0:
        min = 0
    if max < 0:
        max = 0
    return random.randint(min, max)

def getXP(xp: int, cut: float):
    """Returns the amount of xp given"""
    return math.ceil(xp * cut)

def getDrops(lilypad: Lilypad, drop_table):
    """Goes through each drop in a drop table and returns drops"""

    drops = []
    for drop in drop_table:
        id = drop[0]
        chance = drop[1]
        min_amount = drop[2]
        max_amount = drop[3]

        if rollChance(1, 100) <= chance:
            amount = random.randint(min_amount, max_amount)
            drops.append([id, amount])

    for id, amount in drops:
        lilypad.storageAdd(id, amount)

    return True

def checkForSupplies(lilypad: Lilypad, supplies_id):
    """Checks if the respective supplies for the tool exist in players inventory"""
    if (supplies_id is None) or (lilypad.storageFindId(supplies_id) is not None):
        return True
    return False

def getFish(lvl:int, tool:item.Item, available_fish:list):
    """
    Given:
    Fishes available
    Tool Equipped
    Fishing Level
    Returns fish to be caught
    """

    fishes = [
        i
        for i in available_fish
        if i["type"] == tool and i["lvl"] <= lvl
    ]
    if len(fishes) == 0:
        return None
    index = rollChance(0, len(available_fish) - 1)

    return available_fish[index]

def fishing(player: Player, lilypad: Lilypad, times:int=1):
    """"""
    fishing_dict = getJson("fishing")
    tool = player.getTool()
    if tool is None:
        return False
    

    while True:

        if len(lilypad.getStorage()) >= lilypad.getStorageMax():
            lilypad.storageRemove(-1,10000)
            break

        if checkForSupplies(lilypad=lilypad,supplies_id=tool.getSupply()) is False:
            break

        lvl = player.getLevel(player.getFishingXp())
        available_fish = [fishing_dict[str(i)] for i in player.getLocation()['fishing']]

        fish = getFish(lvl=lvl,tool=tool.getTool(),available_fish=available_fish)
        if fish is None:
            return False

        object_lvl = fish["lvl"]
        drop_table = fish["drops"]
        xp = fish["xp"]

        chance = lvl - object_lvl
        if chance <= 0:
            chance = 10
        elif chance > 10:
            chance = 100
        else:
            chance = chance * 10

        while True:
            if rollChance(1, 100) <= chance:
                player.setLogSkill('fishing',fish['name'],'caught',1)
                player.setFishingXp(getXP(xp, 1.0))
                getDrops(lilypad, drop_table)
                break
            else:
                player.setLogSkill('fishing',fish['name'],'attempt',1)

    return True

def cooking(player: Player, lilypad:Lilypad, index:int):
    """"""

    # Check if the item is able to be cooked
    _item = lilypad.storageGetIndex(index)
    item_skills = _item.getSkills()
    if "cooking" not in item_skills:
        return False
    else:
        item_lvl = item_skills['cooking']['lvl']
        cooked_id = item_skills['cooking']['cookID']

    # Check if player is high enough level
    player_lvl = player.getLevel(player.getCookingXp())
    if player_lvl < item_lvl:
        return False

    amount = _item.getAmount()
    cooked = 0
    burnt = 0
    xp = item_skills['cooking']['xp']
    for i in range(amount):
        chance = player_lvl - item_lvl
        if chance <= 0:
            chance = 10
        elif chance > 10:
            chance = 100
        else:
            chance = chance * 10

        if rollChance(1, 100) <= chance:
            cooked += 1
            player.setCookingXp(xp)
        else:
            burnt += 1

    # Remove Raw Item from inventory
    lilypad.storageRemove(index=index,amount=amount)

    if cooked == 0:
        return False
    else:
        # Add item
        lilypad.storageAdd(id=cooked_id,amount=cooked)