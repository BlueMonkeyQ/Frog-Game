import functions
import item
from player import Player
    
def fishing(player: Player, id: int):
    fishing_dict = functions.getJSONSkills("fishing")
    fish_object = fishing_dict[f"{id}"]
    object_lvl = fish_object["lvl"]
    drop_table = fish_object["drops"]
    xp = fish_object["xp"]

    player_lvl = player.getLevel(player.getFishingXp())
    chance = player_lvl - object_lvl
    if chance <= 0: chance = 10
    elif chance > 10: chance = 100
    else: chance = chance*10
    
    print("---------- Fishing ----------")

    if functions.skillCheck(player_lvl, object_lvl):
        while True:
            print("Fishing...")
            if functions.rollChance(1,100) <= chance:
                player.setFishingXp(functions.getXP(xp,1.0))
                drops = functions.getDrops(drop_table)
                for i in drops:
                    id = i[0]
                    amount = i[1]
                    print(f"+{amount} {item.getItemName(id)}")
                    player.inventoryAdd(id,amount)
                break
            else:
                player.setFishingXp(functions.getXP(xp,.2))

    else:
        print(f"Lvl Requirement: {object_lvl}")

    print("----------  ----------")
    


            
            