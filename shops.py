import json
from pathlib import Path

def getJson():
    with open(Path(f"data/shops/shops.json")) as f:
        json_data = f.read()
    return json.loads(json_data)

def getShop(id):
    return shop_dict[str(id)]

shop_dict = getJson()