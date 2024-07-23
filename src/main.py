import maps
from player import Player

def main():
    player = Player()
    # player.inventoryAdd(1,1)
    # player.inventoryRemove(1,1)
    player.inventoryAdd(6,1)
    player.equipEquipment(player.inventoryGetItem(0))
    player.inventoryAdd(2,1)
    player.equipEquipment(player.inventoryGetItem(0))
    player.displayStats()
    maps.worldMap(player, "earth", 1)
    player.displayStats()
    player.inventoryAdd(8,2)
    player.displayStats()
    maps.worldMap(player, "earth", 1)
    player.displayStats()
    player.inventoryAdd(3,1)
    player.equipEquipment(player.inventoryGetItem(1))
    player.inventoryAdd(9,2)
    player.displayStats()
    maps.worldMap(player, "earth", 1)
    player.displayStats()

if __name__ == '__main__':
    main()