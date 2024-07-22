import functions
import json
import item
from player import Player
from pathlib import Path

def getJSONShops():
    with open (Path(f"data/shops/shops.json")) as f:
        json_data = f.read()
    return json.loads(json_data)

shops_dict = getJSONShops()

def getShop(id):
    "Gets the Map Dictionary of the current Planet"
    return shops_dict[f"{id}"]

def getShopName(id):
    "Returns the shops name from shop_dict"
    return shops_dict[f"{id}"]['name']

def getSellValue(id,shop_dict):
    "Returns the sell value of a item given the item and the rate the shop offers"

    # Check if rate exist, if not rate is 1
    base_value = item.item_dict[f"{id}"]['value']
    if id in shop_dict['rate']:
        rate = shop_dict['rate'][f"{id}"]
        return int(base_value * rate)
    else:
        return base_value

def shopMenu(player: Player, id):
    """Menu for interacting with a shop"""
    shop_dict = getShop(id)
    print(f"---------- {shop_dict['name']} ----------")

    buyMenu(player,shop_dict)

    sellMenu(player,shop_dict)

    print(f"---------- {shop_dict['name']} ----------")

def buyMenu(player: Player,shop_dict: dict):
    "Handles the Buying Menu for all shops"

    print(f"----- Buy -----")
    choice = 0
    for id in shop_dict['inventory']:
        choice += 1
        print(f":: [{choice:02d}] ${item.getItemValue(id):<6} {item.getItemName(id)}")
    print(f"----- Buy -----")

def sellMenu(player: Player, shop_dict:dict):
    "Handles the Selling Menu for all shops"
    print(f"----- Sell -----")
    choice = 0
    for i in player.getInventory():
        choice += 1
        print(f":: [{choice:02d}] ${getSellValue(i.getId(),shop_dict):<6} #{i.getAmount()} {i.getName()}")
    print(f"----- Sell -----")