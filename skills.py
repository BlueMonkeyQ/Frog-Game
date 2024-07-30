import functions
import item
import maps
from lilypad import Lilypad, Crew
from player import Player

fishing_dict = functions.getJSONSkills("fishing")


def getDrops(lilypad: Lilypad, drop_table):
    drops = functions.getDrops(drop_table)
    for id, amount in drops:
        lilypad.storageAdd(id, amount)


def checkForSupplies(lilypad: Lilypad, supplies_id):
    """Checks if the respective supplies for the tool exist in players inventory"""
    if (supplies_id is None) or (lilypad.storageFindId(supplies_id) is not None):
        return True
    return False


def getFish(lvl, tool, fishes):
    """
    Given:
    Fishes available
    Tool Equipped
    Fishing Level
    Returns fish to be caught
    """

    fishes = [fishing_dict[f"{i}"] for i in fishes]
    available_fish = [
        i
        for i in fishes
        if i["type"] == tool and i["lvl"] <= lvl
    ]
    if len(available_fish) == 0:
        return None
    index = functions.rollChance(0, len(available_fish) - 1)

    return available_fish[index]


def fishing(player: Player, crew: Crew, lilypad: Lilypad):
    """"""

    tool = crew.getTool()
    if tool is None:
        return False
    
    player_lvl = player.getLevel(player.getFishingXp())
    location = maps.getLocation(player.getLocation())

    fish = getFish(player_lvl,tool.getTool(),location['fishing'])
    if fish is None:
        return False

    object_lvl = fish["lvl"]
    drop_table = fish["drops"]
    xp = fish["xp"]

    chance = player_lvl - object_lvl
    if chance <= 0:
        chance = 10
    elif chance > 10:
        chance = 100
    else:
        chance = chance * 10

    while True:
        if functions.rollChance(1, 100) <= chance:
            player.setLogSkill('fishing',fish['name'],'caught',1)
            player.setFishingXp(functions.getXP(xp, 1.0))
            getDrops(lilypad, drop_table)
            break
        else:
            player.setLogSkill('fishing',fish['name'],'attempt',1)
            player.setFishingXp(functions.getXP(xp, 0.2))

    return True