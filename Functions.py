from Classes import *

def InputQuery():

    Input = input(f'{Player.location.description} \nThe exits are:{Player.location.exits} \nWhat do you want to do? \n\n\n').lower()

    Count = 0 

    for objects in Player.location.objects:

        if objects.name in Input:

            Input = Input.replace(objects.name, ''); Input = Input.replace(" ", "")

            Player.location.objects[Count].checkActions(Input)

            return True

        Count += 1
    
    else:

        Player.location.checkActions(Input)
    