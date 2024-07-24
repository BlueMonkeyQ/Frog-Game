import shops
import skills
from player import Player
from item import Item
from init import player


def testTransaction():
    global player
    shop_dict = shops.getShop(1)

    # Buying - Not enough gold
    assert shops.transaction(player,0,1,1,shop_dict) is False

    # Buying - Enough Gold
    player.setGold(2)
    assert shops.transaction(player,0,1,1,shop_dict) == -2

    # Selling
    assert shops.transaction(player,1,1,1,shop_dict) == 1