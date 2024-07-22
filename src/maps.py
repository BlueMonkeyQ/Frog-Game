import shops
import json
from pathlib import Path

def getJSONMap(planet):
    with open (Path(f"data/maps/{planet}.json")) as f:
        json_data = f.read()
    return json.loads(json_data)

def getPlanetMap(planet):
    "Gets the Map Dictionary of the current Planet"
    return getJSONMap(planet)

def getLocation(map_dict,id):
    """Returns dicitonary of location"""
    return map_dict[f"{id}"]

def worldMap(player, planet):
    """World Map"""

    world_map = getPlanetMap(planet)
    location_dict = getLocation(world_map,1)
    
    print(f"---------- {location_dict['name']} ----------")

    if location_dict['shops']:
        print(f" ----- Shops -----")
        for i in location_dict['shops']:
            print(f":: {shops.getShopName(i)}")
        print(f" ----- Shops -----")

    print(f"---------- {location_dict['name']} ----------")

    shops.shopMenu(player, 1)