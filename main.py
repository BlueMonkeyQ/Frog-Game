import menus
import maps
import item
import json
from character import Player
from lilypad import Lilypad
from pathlib import Path

def main():
    with open(Path(f"data/log/log.json")) as f:
            json_data = f.read()
    player = Player(location=maps.getLocation(1),log=json.loads(json_data))
    player.setToolBelt(item.createItem(4))
    lilypad = Lilypad()
    lilypad.storageAdd(3, 1)
    lilypad.storageAdd(4, 1)
    menus.lilypadHomeScreen(player=player,lilypad=lilypad)

if __name__ == "__main__":
    main()