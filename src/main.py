import skills
import maps
from player import Player

def main():
    player = Player()
    player.displayStats()
    skills.fishing(player,1)
    skills.fishing(player,1)
    maps.worldMap(player, "earth")
    player.inventoryRemove(1,1)
    player.displayStats()

if __name__ == '__main__':
    main()