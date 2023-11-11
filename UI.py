def AddRoom():

    name = input('What would you like the name of your room to be?\n')

    x = input('\nWhat would you like the x coordinate of this room to be?\n')

    y = input('\nWhat would you like the y coordinate of this room to be?\n')

    description = input('\nWhat would you like the description for this room to be?\n')

    AutoExits = input('\nWould you like to enable AutoExits (Automatically adds an exit in the North, East, South and West)? [True/False]\n')
    
    Room = (f'{name} = Areas(\'{name}\',{x},{y},\'{description}\',{AutoExits})')
   
    Actions = input('Would you like to add actions? [y/n]')

    ActionsDict = {}

    if Actions == 'y': 

        while Actions == 'y':

            Trigger = input('What should the trigger be?')

            Action = input('What should the action be? (Remember: Command: and Print: )')

            String = {f'{Trigger}' : f"{Action}"}

            ActionsDict.update(String)

            Continue = input('Would you like to continue? [y/n]')

            if Continue == 'n':

                Actions = False

    Exits = input('Would you like to add exits? [y/n]')
   
    ExitNorth = ''
    
    ExitEast = ''
    
    ExitSouth = ''
    
    ExitWest = ''

    if Exits == 'y':

        while Exits == 'y':

            Temp = input('Which direction should the exit go? [north/east/south/west]')

            Temp2 = input('Where should this exit lead to? [eg. Dungeon1]')

            ExitString = (f'\nAddExit("{Temp}", "{Temp2}", {name})')

            if Temp == 'north':

                ExitNorth = ExitString

            if Temp == 'east':

                ExitEast = ExitString

            if Temp == 'south':

                ExitSouth = ExitString

            if Temp == 'west':

                ExitWest = ExitString
            
            Temp3 = input('Would you like to continue? [y/n]')

            if Temp3 == 'n':

                Exits = False

    return (f'{Room}\nLocation_List.append({name}) \n{name}.actions = {ActionsDict}\n {ExitNorth} {ExitEast} {ExitWest} {ExitSouth}\n \n')


def AddObject():
   
    name = input('What would you like the name of the object to be?\n')
    
    description = input('\nWhat would you like the description for this object to be?\n')
   
    Area = input('What area should this object be assigned to?')

    Actions = input('Would you like to add actions? [y/n]')

    ActionsDict = {}

    if Actions == 'y':

        while Actions == 'y':

            Trigger = input('What should the trigger be?')

            Action = input('What should the action be? (Remember: Command: and Print: )')

            String = {f'{Trigger}' : f"{Action}"}

            ActionsDict.update(String)

            Continue = input('Would you like to continue? [y/n]')

            if Continue == 'n':

                Actions = False

    return (f'{name} = Item\'({name}\', \'{description}\', {Area}) \n{name}.actions = {ActionsDict}')

Loop = True 

while Loop:

    Choice1 = input('Would you like to create a room or an object? [r/o]\n').lower()

    if Choice1 == 'r':
   
        f = open("Rooms.txt", "a+")    
   
        f.write(AddRoom())
     
        f.close()

    if Choice1 == 'o':

        f = open("Objects.txt", "a+")    
     
        f.write(AddObject())
     
        f.close()

    Continue = input('Continue? [y/n] \n').lower()

    if Continue == 'n':
   
        Loop = False

