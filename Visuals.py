from Classes import *

Exits = Player.location.exits

LocationASCIIArt = ['---------', '|       |\n' f'| {Player.location.name} |', '|       |', '---------']

for i in LocationASCIIArt:
    print(i)

if 'north' in Exits:

    for item in Location_List:

        if item.x == Player.location.x and item.y == Player.location.y+1:

            print(item.name)



