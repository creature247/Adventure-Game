import time
import os

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

class Player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

class Item(object):
    def __init__(self, name, description, is_movable):
        self.name = name
        self.description = description
        self.is_movable = is_movable

stone = Item("stone", "A small stone in the middle of the clearing.", True)
book = Item("book","A book is standing on a shelf in the tree house, looks like you can pull it.",False)
tree = Item("tree","A tree looks like you could bang a stone on it.",False)
diamond = Item("diamond","A shiny diamond which is upside down pointing in the sky",False)
hole = Item("hole","A deep hole that wasn't there before. You can see something gleaming at the bottom.",False)
bush = Item("bush","A bush you can put your hand in it.",False)
squirrel = Item("squirrel","An angry squirrel",False)
button = Item("button","A button next to the diamond. you can press the button.",False)
spacesuit = Item("spacesuit","A space suit is sitting in the corner of the room.",True)
controlpanel = Item("controlpanel","A complicated control panel covered in buttons and switches, you might be able to use it to get home",False)

clearing = Room("Clearing","You are standing in the middle of a clearing in the woods.")
clearing.items.append(stone)

forest_east = Room("Forest to the east","You are still in the forest")
forest_east.items.append(tree)

forest_north = Room("Forest to the north","You are still in the forest")
forest_north.items.append(bush)

treehouse = Room("Abandoned tree house","You are in a into an abandoned tree house" )
treehouse.items.append(book)

secretroom = Room("Secret room","This secret room looks like it has been abamdoned for years")
secretroom.items.append(diamond)
secretroom.items.append(button)
secretroom.items.append(spacesuit)

clearing.exits["east"]= forest_east
forest_east.exits["west"]= clearing
treehouse.exits["down"]= forest_east
secretroom.exits["up"]= forest_east
clearing.exits["north"]= forest_north
forest_north.exits["south"]= clearing

player = Player("The Player", clearing)

print("Welcome to My little Adventure")
print("\nYou wake up in a clearing.")

while True:
    print("")
    print(player.location.name)
    print(player.location.description)
    print("\nHere are the exits: ")
    for exit in player.location.exits:
        print(exit)
    print("\nYou see the following: ")
    for item in player.location.items:
        print(item.name)

    try:
        command = raw_input("\n> ")
    except:
        command = input("\n> ")
        
    words = command.split()
    if len(words) > 0:
        verb = words[0]
    if len(words) > 1:
        noun = words[1]

    if verb == "look":
        for item in player.location.items:
            if item.name == noun:
                print(item.description)
        for item in player.inventory:
            if item.name == noun:
                print(item.description)

    if verb == "get":
        for item in player.location.items:
            if item.name == noun:
                # Check is it movable
                if item.is_movable:
                    print("You take the {}".format(item.name))
                    # Remove from room
                    player.location.items.remove(item)
                    # Add to player's inventory
                    player.inventory.append(item)
                
                else:
                    print("Sorry, you can't move that.")

    if verb == "drop":
       for item in player.inventory:
            print("You drop the {}.".format(item.name))
            player.inventory.remove(item)
            player.location.items.append(item)

    if verb in ["inv", "inventory"]:
        print("You have the following: ")
        for item in player.inventory:
            print(item.name)

    if verb in ["north", "south", "east", "west", "up", "down"]:
        if verb in player.location.exits:
            player.location = player.location.exits[verb]
            print("You go {} and find yourself in a new place.".format(verb))

    if player.location == forest_east:
        if verb == "use" and noun == "stone":
            if stone in player.inventory:
                print("You bang the stone on the tree the stone breaks and a lader falls from the sky.")
                player.inventory.remove(stone)
                forest_east.exits["up"] = treehouse
            else:
                print("You do not have a stone.")

    if player.location == treehouse:
        if verb == "use" and noun == "book":
            print("You pull the book and you hear a secret passageway open up")
            player.location.items.remove(book)
            forest_east.items.append(hole)
            forest_east.exits["down"] = secretroom

    if player.location == forest_north:
        if verb == "use" and noun == "bush":
            print("You put your hand in the bush, a squirrel runs out")
            player.location.items.remove(squirrel)
            forest_north.items.append(squirrel)

    if player.location == secretroom:
        if verb == "use" and noun == "button":
            print("You press the button and a lazer is shot into the sky and deflects off a satalite holowing out the treehouse clearing and everything else you have seen since you woke up.")
            if spacesuit in player.inventory:
                print("the island flies into space and the clearing seems to change. You need to get home")
                clearing.items.append(controlpanel)
            else:
                print("the island flies into space and the clearing changes as you choke to death.")
                time.sleep(3)
                print("Clue: put on the spacesuit")
                time.sleep(1)
                os.system('clear')

    if player.location == clearing:
        if controlpanel in player.location.items:
            if verb == "use" and "controlpanel":
                print("you can do many things sutch as: east north south west.")