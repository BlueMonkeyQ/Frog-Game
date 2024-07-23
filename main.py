import maps
from player import Player

def main():
    player = Player()
    player.displayStats()
    maps.worldMap(player, "earth", 1)

if __name__ == '__main__':
    main()