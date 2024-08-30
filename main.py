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
    tool = item.createItem(3)
    player.setTool(tool)
    lilypad = Lilypad()
    menus.lilypadHomeScreen(player=player,lilypad=lilypad)
    # menus.shopScreen(player=player,lilypad=lilypad,shop_id=1)

if __name__ == "__main__":
    main()