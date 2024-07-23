import functions
import item
from player import Player

fishing_dict = functions.getJSONSkills("fishing")

def getDrops(player: Player, drop_table):
    drops = functions.getDrops(drop_table)
    for id, amount in drops:
        print(f"+{amount} {item.getItemName(id)}")
        player.inventoryAdd(id,amount)

def checkForSupplies(player: Player, supplies_id):
    """Checks if the respective supplies for the tool exist in players inventory"""
    if (supplies_id is None) or (player.inventoryFindItem(supplies_id) is not None):
        return True
    return False

def getFish(player: Player, tool_type, fishes):
    """
    Given:
    Fishes available
    Tool Equipped
    Fishing Level
    Returns fish to be caught
    """
    
    fishes = [fishing_dict[f"{i}"] for i in fishes]
    available_fish = [i for i in fishes if i['type'] == tool_type]
    if len(available_fish) == 0: return None
    index = functions.rollChance(0,len(available_fish)-1)

    return available_fish[index]
        

def fishingMenu(player: Player, location_dict):
    """Menu for interacting with a fishing skill"""

    # Check if player has fishing tool equipped
    if player.getTool().getToolType() in ['net','fly','spear','fishing']:
        # Check if player has supplies
        tool = player.getTool()
        tool_type = tool.getToolType()
        supplies_id = tool.getToolSupplies()
        if checkForSupplies(player, supplies_id) is True:
            fish = getFish(player,tool_type,location_dict['fishing'])
            if fish is None:
                return 0
            else:
                player.inventoryRemove(supplies_id,1)
                fishing(player, fish)
        else:
            print(f"Missing Supply: {item.getItemName(supplies_id)}")


def fishing(player: Player, fish: dict):
    """Handles catching a fish"""

    object_lvl = fish["lvl"]
    drop_table = fish["drops"]
    xp = fish["xp"]

    player_lvl = player.getLevel(player.getFishingXp())
    chance = player_lvl - object_lvl
    if chance <= 0: chance = 10
    elif chance > 10: chance = 100
    else: chance = chance*10
    
    print("---------- Fishing ----------")

    if functions.skillCheck(player_lvl, object_lvl):
        while True:
            print("Fishing...")
            if functions.rollChance(1,100) <= chance:
                print("Caught!")
                player.setFishingXp(functions.getXP(xp,1.0))
                getDrops(player, drop_table)
                break
            else:
                player.setFishingXp(functions.getXP(xp,.2))

    else:
        print(f"Lvl Requirement: {object_lvl}")

    print("----------  ----------")