import shops
import skills
import json
from pathlib import Path

def getJson():
    with open(Path(f"data/maps/map.json")) as f:
        json_data = f.read()
    return json.loads(json_data)

def getLocation(id):
    return map_dict[str(id)]

map_dict = getJson()