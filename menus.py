import time
import threading
from typing import List
import maps
import shops
import skills
import item
from character import Player
from lilypad import Lilypad
from rich.live import Live
from rich.console import Console, group
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.columns import Columns
from rich.layout import Layout
from rich.progress import Progress, BarColumn, TextColumn
from rich import print

def buildMenu(options):
    table = Table.grid(expand=True)
    padded_options = [f"{option}{' ' * 2}" for option in options]
    for i in padded_options:
        table.add_column(justify='center')
    table.add_row(*padded_options)
    return table

def buildLocation(player: Player):
    tabel = Table()
    return tabel

def buildCharacter(player: Player):
    table = Table.grid()
    table.add_row(f"Gold        {player.getGold()}")
    table.add_row(f"Fishing Lvl {player.getLevel(player.getFishingXp()):<2} {player.getFishingXp():>7}xp")
    table.add_row(f"Cooking Lvl {player.getLevel(player.getCookingXp()):<2} {player.getCookingXp():>7}xp")
    table.add_row(f"Tool        {player.getTool().getName() if player.getTool() is not None else 'None'}")
    return table

def buildLilypad(lilypad: Lilypad):
    table = Table.grid()
    return table

def buildLilypadInventory(lilypad: Lilypad):
    general_stoarge = lilypad.getStorage()
    general_table = Table.grid()
    general_table.add_column("General")
    for indx, i in enumerate(general_stoarge):
        general_table.add_row(f"{indx+1}| #{i.getAmount()} {i.getName()}")
    
    main_table = Table.grid()
    main_table.add_row(general_table)
    return main_table

def buildTravel(player:Player):
    pass

def buildShops(player:Player):
    pass

def buildShop(shop_dict):
    items: List[item.Item] = []
    for i in shop_dict['inventory']:
        items.append(item.getItem(i))
    
    table = Table.grid()
    for indx, i in enumerate(items):
        table.add_row(f"{indx+1}| {i['name']} Gold: {i['value']}")
    return table
    
def getInput(options):
    user_input = Prompt.ask(">")
    if user_input.isdigit() and 1 <= int(user_input) <= len(options):
        selected_option = options[int(user_input) - 1]
    else:
        return False
    return selected_option

def getMultiInput(options):
    console = Console()
    user_input = Prompt.ask(">")
    sections = user_input.split()

    if len(sections) == 0:
        return False

    try:
        action = options[int(sections[0]) - 1]
    except IndexError:
        return False
    
    if action == "Back":
        return ["Back"]
    
    elif action == "Buy" or action == "Sell":

        if len(sections) != 3:
            console.print("[red]Buy/Sell Item Position Amount[/red]")
            return False

        if not (sections[0].isdigit() and 1 <= int(sections[0]) <= len(options)):
            console.print("[red]Invalid Buy/Sell Option[/red]")
            return False
        sections[0] = action

        if not sections[1].isdigit():
            console.print("[red]Invalid Item Position[/red]")
            return False

        if not sections[2].isdigit():
            console.print("[red]Invalid Amount[/red]")
            return False
        
    elif action == "Cook":
        if len(sections) != 2:
            console.print("[red]Cook Item Position Amount[/red]")
            return False
        
        if not (sections[0].isdigit() and 1 <= int(sections[0]) <= len(options)):
            console.print("[red]Invalid Cook Option[/red]")
            return False
        sections[0] = action

        if not sections[1].isdigit():
            console.print("[red]Invalid Item Position[/red]")
            return False
    
    return sections
        
def buildScreen(player: Player,lilypad: Lilypad, options: list,
                show_character=False,show_inv=False,show_shop=False,
                shop_dict=None):
    layout = Layout()

    layout.split_column(
            Layout(name="location"),
            Layout(name="character"),
            Layout(name='inventory'),
            Layout(name='shop'),
            Layout(name="input")
        )
    
    layout['location'].split_row(
        Layout(Panel(buildLocation(player),title=player.getLocation()['name'],border_style="bold blue"))
    )
    layout['location'].size = 2
    layout['location'].visible = True
    
    layout['character'].split_row(
            Layout(Panel(buildCharacter(player),title="Frog",border_style="bold blue")),
            Layout(Panel(buildLilypad(lilypad),title="Lilypad",border_style="bold blue"))
        )
    layout['character'].size = 6
    layout['character'].visible = show_character

    layout['inventory'].split_row(
        Layout(Panel(buildLilypadInventory(lilypad),title="Inventory",border_style="bold blue"))
    )
    layout['inventory'].size = 15
    layout['inventory'].visible = show_inv

    layout['shop'].visible = show_shop
    if show_shop is True:
        layout['shop'].split_row(
                Layout(Panel(buildLilypadInventory(lilypad),title="Inventory",border_style="bold blue")),
                Layout(Panel(buildShop(shop_dict),title=shop_dict['name'],border_style="bold blue"))
            )
        layout['shop'].size = 12

    layout['input'].split_column(
        Layout(Panel(buildMenu(options=options),title="Options"))
    )
    layout['input'].size = 3
    print(layout)

def lilypadHomeScreen(player:Player, lilypad:Lilypad):
    options = []

    if len(player.getLocation()['fishing']) >= 1:
        options.append("Fishing")
    if lilypad.getStove() is True:
        options.append("Cook")
    options.extend(["Inventory","Fishing Shop","Quit"])
    while True:

        buildScreen(player=player,lilypad=lilypad,options=options,
                    show_character=True)
        choice = getInput(options)

        if choice == "Fishing":
            lilypadFishScreen(player=player,lilypad=lilypad)

        elif choice == "Cook":
            lilypadCookScreen(player=player,lilypad=lilypad)

        elif choice == 'Inventory':
            lilypadInventoryScreen(player=player,lilypad=lilypad)

        elif choice == "Fishing Shop":
            shopScreen(player=player,lilypad=lilypad,shop_id=1)

        elif choice == 'Quit':
            return 0

def lilypadInventoryScreen(player:Player, lilypad:Lilypad):
    options = [
        "Back"
    ]

    while True:

        buildScreen(player=player,lilypad=lilypad,options=options,
                    show_character=True,show_inv=True)
        choice = getInput(options)

        if choice == 'Back':
            return 0

def lilypadFishScreen(player:Player, lilypad:Lilypad):
    skills.fishing(player=player, lilypad=lilypad, times=1)

def lilypadCookScreen(player:Player, lilypad:Lilypad):

    while True:
        options = [
            "Cook",
            "Back"
        ]
        buildScreen(player=player,lilypad=lilypad,options=options,
                    show_character=True,show_inv=True)
        choices = getMultiInput(options=options)

        if choices is False:
            continue
        
        if choices[0] == "Back":
            break

        index = int(choices[1]) - 1
        skills.cooking(player=player,lilypad=lilypad,index=index)

def lilypadTravelScreen(player:Player, lilypad:Lilypad):
    pass

def shopScreen(player:Player, lilypad:Lilypad, shop_id:int):
    shop_dict = shops.getShop(shop_id)
    items_dict: List[item.Item] = []
    for i in shop_dict['inventory']:
        items_dict.append(item.getItem(i))
    while True:
        options = [
            "Buy",
            "Sell",
            "Back"
        ]
        buildScreen(player=player,lilypad=lilypad,options=options,
                    show_character=True,show_shop=True,
                    shop_dict=shop_dict)
        choices = getMultiInput(options)
        
        if choices is False:
            continue
        
        if choices[0] == "Back":
            break
        
        action = choices[0]
        index = int(choices[1])
        quantity = int(choices[2])

        # If buying
        # Check if the item index exist
        # Then buy the maximum amount the user can get if the amount > then they have in gold
        if (action == "Buy") and (1 <= int(index) <= len(items_dict)):
            value = items_dict[index-1]['value']
            amount = player.getGold() // value
            amount = min(amount,quantity)
            if amount == 0:
                continue
            gold = value * amount
            player.setGold(-gold)

            # If there is not room in the players inventory, 
            # return the gold amount
            amount = lilypad.storageAdd(shop_dict['inventory'][index-1],amount)
            if amount >= 1:
                gold = value * amount
                player.setGold(gold)

        # Selling
        # Sell the maximum amount if the quantity is over the amount
        elif (action == "Sell") and (1 <= int(index) <= len(lilypad.getStorage())):
            _item = lilypad.storageGetIndex(index-1)
            if quantity >= _item.getAmount():
                quantity = _item.getAmount()

            gold = quantity * _item.getValue()
            player.setGold(gold)
            lilypad.storageRemove(index-1,quantity)