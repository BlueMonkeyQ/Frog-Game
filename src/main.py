import skills
import maps
from player import Player

def main():
    player = Player()
    maps.worldMap(player, "earth")
    player.inventoryAdd(1,1)
    player.inventoryRemove(1,1)
    player.inventoryAdd(6,1)
    player.displayStats()
    player.equipEquipment(player.inventoryGetItem(0))
    player.inventoryAdd(2,1)
    player.equipEquipment(player.inventoryGetItem(0))
    player.displayStats()

if __name__ == '__main__':
    main()