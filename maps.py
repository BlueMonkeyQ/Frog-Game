import shops
import skills
import json
from pathlib import Path

def getJSONMap(planet):
    with open (Path(f"data/maps/{planet}.json")) as f:
        json_data = f.read()
    return json.loads(json_data)

def getPlanetMap(planet):
    "Gets the Map Dictionary of the current Planet"
    return getJSONMap(planet)

def getLocation(world_map,id):
    """Returns dicitonary of location"""
    return world_map[f"{id}"]

def worldMap(player, planet, id):
    """World Map"""

    world_map = getPlanetMap(planet)
    location_dict = getLocation(world_map,2)
    
    print(f"---------- {location_dict['name']} ----------")

    if 'shops' in location_dict:
        print(f" ----- Shops -----")
        for i in location_dict['shops']:
            print(f":: {shops.getShopName(i)}")
        print(f" ----- Shops -----")

    if 'areas' in location_dict:
        print(f" ----- Areas -----")
        for i in location_dict['areas']:
            print(f":: {world_map[f"{i}"]['name']}")
        print(f" ----- Areas -----")

    print(f"---------- {location_dict['name']} ----------")

    shops.shopMenu(player, 1)
    skills.fishingMenu(player,location_dict)