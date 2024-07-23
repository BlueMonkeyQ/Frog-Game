import maps as maps
import skills
from player import Player
from item import Item
from init import player


def testFishingMenu():
    global player
    world_map = maps.getPlanetMap('earth')
    location_dict = maps.getLocation(world_map,2)

    # No Equipment
    assert skills.fishingMenu(player, location_dict) is None

    # ----- With tool -----
    # No Supplies
    player.inventoryAdd(2,1)
    player.equipEquipment(player.inventoryFindItem(2))
    assert skills.fishingMenu(player, location_dict) is None
    assert player.inventoryFindItem(10) is None

    # Supplies
    player.inventoryAdd(8,1)
    assert skills.fishingMenu(player, location_dict) is True
    assert player.inventoryFindItem(8) is None
    assert player.inventoryFindItem(10).getId() == 10