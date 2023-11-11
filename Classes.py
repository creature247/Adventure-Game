def AutoLocations():

    if Player.location.AutoExits == True:
    
        for item in Location_List:

            if item.x == Player.location.x and item.y == Player.location.y+1:

                string = {'move north' :  "Command:Player.location = " + item.name}

                Player.location.actions.update(string)


            if item.x == Player.location.x and item.y == Player.location.y-1:

                string = {'move south' :  "Command:Player.location = " + item.name}

                Player.location.actions.update(string)

        
            if item.x == Player.location.x+1 and item.y == Player.location.y:

                string = {'move east' :  "Command:Player.location = " + item.name}

                Player.location.actions.update(string)


            if item.x == Player.location.x-1 and item.y == Player.location.y:

                string = {'move west' :  "Command:Player.location = " + item.name}

                Player.location.actions.update(string)
            
        if 'move north' in Player.location.actions:

            Player.location.exits.append('north')

        if 'move east' in Player.location.actions:

            Player.location.exits.append('east')

        if 'move south' in Player.location.actions:

            Player.location.exits.append('south')

        if 'move west' in Player.location.actions:

            Player.location.exits.append('west')


def AddExit(direction,location,Area):

    string = {f'move {direction}' :  "Command:Player.location = " + location}

    Area.actions.update(string)
    
    Area.exits.append(direction)

class Areas():

    def __init__(self, name, x, y, description, AutoExits):
        
        self.name = name

        self.description = description

        self.exits = []

        self.x = x

        self.y = y

        self.actions = None
        
        self.objects = []

        self.AutoExits = AutoExits


    def checkActions(self, Input_String):

        if Input_String in self.actions:

            returnedValue = self.actions[Input_String]

            if 'Command:' in returnedValue:

                returnedValue = returnedValue.replace('Command:', '')

                exec(returnedValue)

            if 'Print:' in returnedValue:

                returnedValue = returnedValue.replace('Print:', '')

                print(returnedValue)   

        else:
            return

class Item():

    def __init__(self, name, description, Area):

        Area.objects.append(self)    

        self.name = name

        self.description = description
    
        self.actions = None

    def checkActions(self, Input_String):

        if Input_String in self.actions:

            returnedValue = self.actions[Input_String]

            if 'Command:' in returnedValue:

                returnedValue = returnedValue.replace('Command:', '')

                exec(returnedValue)

            if 'Print:' in returnedValue:

                returnedValue = returnedValue.replace('Print:', '')

                print(returnedValue)
        
        else:
            return

class PlayerClass():
    def __init__(self):
        self.location = None


Player = PlayerClass() 
Player.location = None

Location_List = []

f = open("Rooms.txt", "r")
for x in f:
  exec(x) 

f = open("Objects.txt", "r")
for x in f:
  exec(x) 

Player.location = Room1



    


