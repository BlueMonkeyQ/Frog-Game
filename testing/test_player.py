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

def testBank():
    player = Player()

    # Adding item to bank
    assert player.bankAdd(2,100) is True
    assert player.bankFindItem(2).getAmount() == 100

    # Removing item from bank
    assert player.bankRemove(2,50) is True
    assert player.bankFindItem(2).getAmount() == 50

    # Removing item from Bank with amount over what we have
    assert player.bankRemove(2,100) is True
    assert player.bankFindItem(2) is None

    # Adding item from Inventory to bank
    player.inventoryAdd(8,2)
    assert player.inventoryToBank(8,1) is True
    assert player.bankFindItem(8).getAmount() == 1
    assert player.inventoryFindItem(8).getAmount() == 1

    # Adding item from Inventory to bank removing Item
    assert player.inventoryToBank(8,1) is True
    assert player.bankFindItem(8).getAmount() == 2
    assert player.inventoryFindItem(8) is None

    # Adding item from Inventory to bank with amount over what we have
    player.inventoryAdd(1,1)
    assert player.inventoryToBank(1,100) is True
    assert player.bankFindItem(1).getAmount() == 1

    # Adding item from Bank to Inventory
    assert player.bankAdd(2,1) is True
    assert player.bankToInventory(2,1) is True
    assert player.inventoryFindItem(2).getAmount() == 1

    # Adding item from Bank to Inventory removing item
    assert player.bankAdd(3,1) is True
    assert player.bankToInventory(3,1) is True
    assert player.bankFindItem(3) is None

    # Adding item from Bank to Inventory with remainder
    assert player.bankAdd(7,100) is True
    assert player.bankToInventory(7,100) is True
    assert len(player.getInventory()) == player.getInventoryMax()
    assert player.bankFindItem(7).getAmount() == 98

    # Adding item from Bank to Inventory with amount over what we have
    assert player.inventoryRemove(2,1) is True
    assert player.bankAdd(9,1) is True
    assert player.bankToInventory(9,100) is True
    assert len(player.getInventory()) == player.getInventoryMax()
    assert player.bankFindItem(9) is None

    # Adding item from Bank to Inventory but inventory is full
    assert player.bankToInventory(9,100) is False
    assert len(player.getInventory()) == player.getInventoryMax()