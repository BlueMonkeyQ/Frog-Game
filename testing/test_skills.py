import maps as maps
import skills
from player import Player


def testFishingMenu():
    player = Player()
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
    assert player.getLog()['skills']['fishing']['Sardine']['caught'] == 0

    # Supplies
    player.inventoryAdd(8,2)
    assert skills.fishingMenu(player, location_dict) is True
    assert player.inventoryFindItem(10).getId() == 10
    assert player.getLog()['skills']['fishing']['Sardine']['caught'] == 1
    assert skills.fishingMenu(player, location_dict) is True
    assert player.getLog()['skills']['fishing']['Sardine']['caught'] == 2
    assert player.inventoryFindItem(8) is None