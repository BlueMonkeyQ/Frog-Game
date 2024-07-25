import item
from player import Player

def testEquipEquipment():
    player = Player()

    # Equipping Tool
    equipment = item.itemFromJson(item.getItem(2),2)
    assert player.equipEquipment(equipment) is True
    assert player.getTool().getId() == 2

    # Equipping Tool when 1 is already equipped
    equipment = item.itemFromJson(item.getItem(4),4)
    assert player.equipEquipment(equipment) is True
    assert player.getTool().getId() == 4
    assert player.getInventory()[0].getId() == 2

    # Backpack
    equipment = item.itemFromJson(item.getItem(15),15)
    assert player.equipEquipment(equipment) is True
    assert player.getInventoryMax() == 50
    assert player.getBackpack().getId() == 15

    # High Tier Backback to Low Tier
    player.inventoryAdd(1,500)
    equipment = item.itemFromJson(item.getItem(6),6)
    assert player.equipEquipment(equipment) is False
    
    # Equipping Item that is NOT a tool or backpack
    equipment = item.itemFromJson(item.getItem(1),1)
    assert player.equipEquipment(equipment) is False
    assert player.getTool().getId() == 4
    assert player.getBackpack().getId() == 15