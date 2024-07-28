import shops
from player import Player


def testTransaction():
    player = Player()
    shop_dict = shops.getShop(1)

    # Buying - Not enough gold
    assert shops.transaction(player,0,1,1,shop_dict) is False

    # Buying - Enough Gold
    player.setGold(4)
    assert shops.transaction(player,0,1,1,shop_dict) == -2
    assert player.getLog()['gold']['spent'] == 2

    assert shops.transaction(player,0,1,1,shop_dict) == -2
    assert player.getLog()['gold']['spent'] == 4

    # Selling
    assert shops.transaction(player,1,1,1,shop_dict) == 1
    assert player.getLog()['gold']['earned'] == 1

    assert shops.transaction(player,1,1,1,shop_dict) == 1
    assert player.getLog()['gold']['earned'] == 2