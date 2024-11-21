import time

win = False
hasQuit = False
loc = "Commons" 
# Commons, Hallway, Gym, Cafeteria, Office, Treasure Room
inventory = []
isHallwayBroken = False
hasCutFence = False
hasOpenedDrawer = False
hasUnlockedBox = False
hasSolvedPuzzle = False


items = {
    "hammer": "Commons",
    "key": "Gym",
    "chain cutters": "Cafeteria",
    "card": "Office",
}

inspectables = {
    "clock": "Commons",
    "wall": "Hallway",
    "chain": "Gym",
    "drawer": "Office",
    "locked box": "Treasure Room",
    "computer": "Treasure Room",
}

def changeLocation(newloc):
    global loc
    loc = newloc

def check(check):
    global loc
    return check == loc

def introScene():
    print('Welcome to the Adventure!')
    print('You can start by typing "look" to see your surroundings.')
    print('You can also type "help" for a list of commands.')
    print('Good luck!')

def helpScene():
    print('Commands:')
    print('\tlook - Look around the room')
    print("\tgo - Move in a direction")
    print('\tnorth, south, east, west - Chose a direction to go')
    print('\ttake - Take an item')
    print('\tuse - Use an item')
    print("\tinspect - Inspect something you see")
    print('\tinventory - Check your inventory')
    print('\thelp - Display this message')
    print('\tpassword - Enter a password')
    print('\tanswer - Give answers to puzzles')
    print('\tremove - Remove an item from your inventory')

def lookScene():
    
    global loc
    global isHallwayBroken
    global hasCutFence
    global hasOpenedDrawer
    global hasUnlockedBox
    global isFirstTimeInTreasureRoom
    
    match loc:
        case "Commons":
            print('You are in a large, dimly lit room.')
            print("You can see the clear night sky through the windows above.")
            print("You see a clock to your left and a hammer to your right.")
        case "Hallway":
            if not isHallwayBroken:
                print("You are in what appears to be a long hallway.")
                print("You cannot see anything past the large wall in front of you.")
                print("It appears as if a hammer could break through the wall.")
            else:
                print("You are in what appears to be a long hallway.")
                print("You see five doors, two to the east and one in each other direction.")
        case "Gym":
            if not hasCutFence:
                print("You are in a large, brightly lit basketball gym.")
                print("You see a chain link fence behind which is a key.")
                print("It appears that you might need something to cut the chain.")
            else:
                print("You are in a large, brightly lit basketball gym.")
        case "Cafeteria":
            print("You are in a large, dark room which appears to be a cafeteria.")
            print("You see folded tables and chairs in the corner.")
            print("You are starting to see unusual shapes in the darkness through the windows.")
            print("You notice a pair of chain cutters on the floor near the wall.")
        case "Office":
            if not hasOpenedDrawer:
                print("You are in a small, cluttered office.")
                print("It appears that someone has been here recently, but there is no one in sight.")
                print("There appears to be a key-locked drawer in the desk.")
            else:
                print("You are in a small, cluttered office.")
                print("It appears that someone has been here recently, but there is no one in sight.")
                print("The drawer in the desk is open.")
        case "Treasure Room":
            if not hasUnlockedBox:
                print("You are in a seemingly endless room filled with computers.")
                print('One computer in the distance is turned on.')
                print("The only space without a computer is a small desk with a keycard-locked box on it.")
            else:
                print("You are in a seemingly endless room filled with computers.")
                print("The only space without a computer is a small desk with the opened box on it.")
                print("You see more computers turned on.")
                print("All except the one in the distance have the same message: a clock counting down from 5 minutes.")
                print("Seems as if you have limited time.")

def go(dir):
    
    global isHallwayBroken
    
    match dir:
        case "north":
            if check("Hallway") and isHallwayBroken:
                changeLocation("Treasure Room")
                print("You walk through the door to the north.")
            elif check("Hallway") and not isHallwayBroken:
                print("You find yourself up against a wall.")
            elif check("Gym"):
                changeLocation("Hallway")
                print("You walk through the door to the north.")
            else:
                print("You cannot go that way.")
        case "west":
            if check("Hallway") and isHallwayBroken:
                print("There are two doors to the west.")
                print("Say 'sw' to go through the south one and 'nw' to go through the north one.")
            elif check("Hallway") and not isHallwayBroken:
                changeLocation("Commons")
                print("You walk through the door to the west.")
            elif check("Gym"):
                changeLocation("Hallway")
                print("You walk through the door to the west.")
            elif check("Office"):
                changeLocation("Hallway")
                print("You walk through the door to the west.")
            else:
                print("You cannot go that way.")
        case "south":
            if check('Treasure Room'):
                changeLocation("Hallway")
                print("You walk through the door to the south.")
            elif check("Hallway") and isHallwayBroken:
                changeLocation("Gym")
                print("You walk through the door to the south.")
            else:
                print("You cannot go that way.")
        case "east":
            if check("Commons"):
                changeLocation("Hallway")
                print("You walk through the door to the east.")
            elif check("Hallway") and isHallwayBroken:
                changeLocation("Office")
                print("You walk through the door to the east.")
            elif check("Cafeteria"):
                changeLocation("Hallway")
                print("You walk through the door to the east.")
            else:
                print("You cannot go that way.")
                
def inspect(inspect):
    
    global loc
    global inspectables
    if inspectables[inspect] == loc:
        if inspect == "wall":
            print("The wall appears to be made of a thin but sturdy material.")
            print("It looks like it could be broken by a hammer.")
        elif inspect == "chain":
            print("The chain is made of a thick metal.")
            print("There is a key on the other side of the fence, but you cannot reach it.")
        elif inspect == "drawer":
            print("The drawer is locked.")
            print("There is a card slot on the front.")
        elif inspect == "locked box":
            print("The box is made of a sturdy metal.")
            print("There is a card slot on the front.") 
        elif inspect == "computer":
            print("The computer is turned on and is prompting you for a password.")
    else:
        print("What?")

def take(item):
    global inventory
    global items
    if item in items and check(items[item]):
        inventory.append(item)
        print(f"You take the {item}.")
        items.pop(item)
        
def use(item):
    
    global isHallwayBroken
    global hasCutFence
    global hasOpenedDrawer
    global hasUnlockedBox
    
    if item == "hammer" and check("Hallway"):
        print("You swing the hammer at the wall and it breaks through!")
        print("A long hallway is revealed.")
        isHallwayBroken = True
        inspectables.pop("wall")
        inventory.pop(inventory.index("hammer"))
    elif item == "chain cutters" and check("Gym"):
        print("You cut the chain. There is a key on the other side.")
        hasCutFence = True
        inventory.pop(inventory.index("chain cutters"))
    elif item == "key" and check("Office"):
        print("You unlock the drawer and find a card.")
        hasOpenedDrawer = True
        inventory.pop(inventory.index("key"))
    elif item == "card" and check("Treasure Room"):
        print("You unlock the box.")
        print("Inside is a paper with a password: 'lol'.")
        print("You can type 'password [password]' to enter the password.")
        hasUnlockedBox = True
        inventory.pop(inventory.index("card"))
            
def passwordScene():
    if check("Treasure Room"):
        print("You have entered the correct password.")
        print("\tYou are greeted with yet another puzzle: 'What is the derivative of x^3?'")
        print("Type 'answer [your answer]' to give your answer.")
    else:
        print("What?")
        
def quitScene():
    global hasQuit
    print("You have quit the game.")
    print("You've escaped, but not for long...")
    hasQuit = True
        
def remove(item):
    global inventory
    inventory.pop(inventory.index(item))
    print(f"You remove the {item} from your inventory.")
    
def loseScene():
    if not isHallwayBroken and "hammer" not in inventory and "hammer" not in items:
        print("You have lost.")
        print("You can type quit to exit the game.")
    if not hasCutFence and "chain cutters" not in inventory and "chain cutters" not in items:
        print("You have lost.")
        print("You can type quit to exit the game.")
    if not hasOpenedDrawer and "key" not in inventory and "key" not in items:
        print("You have lost.")
        print("You can type quit to exit the game.")
    if not hasUnlockedBox and "card" not in inventory and "card" not in items:
        print("You have lost.")
        print("You can type quit to exit the game.")

introScene()

while not win and not hasQuit:
    loseScene()
    userinput = input('').lower()
    
    if "go" in userinput:
        if "north" in userinput:
            go("north")
        elif "south" in userinput:
            go("south")
        elif "east" in userinput:
            go("east")
        elif "west" in userinput:
            go("west")
        elif "nw" in userinput:
            changeLocation("Cafeteria")
            print("You walk through the door to the northwest.")
        elif "sw":
            changeLocation("Office")
            print("You walk through the door to the southeast.")
        else:
            print("Invalid direction.")
    
    elif "look" in userinput:
        lookScene()
    
    elif "help" in userinput:
        helpScene()
        
    elif "inspect" in userinput:
        if "clock" in userinput:
            print("To see the clock, you must solve a puzzle:")
            print('\tSin^2 θ = 1/4. Solve for θ on the interval [0, π/2].')
            print("Type 'answer [your answer]' to give your answer.")
        elif "wall" in userinput:
            inspect("wall")
        elif "chain" in userinput:
            inspect("chain")
        elif "drawer" in userinput:
            inspect("drawer")
        elif "locked box" in userinput:
            inspect("locked box")
        elif "computer" in userinput:
            inspect("computer")
        else:
            print("Invalid item.")
            
    elif "answer" in userinput:
        if check("Commons"):
            if "π/6" in userinput or "pi/6" in userinput or "30 degrees" in userinput or "30" in userinput or "π/6 radians" in userinput or "pi/6 radians" in userinput:
                print("Correct. The clock reads midnight.")
                print("How long have I been here?")
            else:
                print("Incorrect.")
        if check("Treasure Room"):
            if "3x^2" in userinput:
                print("You have entered the correct answer.")
                print("The computer displays a message: 'You have 5 minutes to leave the building.'")
                print("You hear a loud noise and the lights go out.")
                print("You feel the ground shake...\n")
                time.sleep(1)
                print("You wake up in a cold sweat.")
                print("It was all a dream.")
                win = True
    
    elif "take" in userinput:
        if "hammer" in userinput:
            take("hammer")
        elif "chain cutters" in userinput:
            take("chain cutters")
        elif "key" in userinput:
            take("key")
        elif "card" in userinput:
            take("card")
        else:
            print("Invalid item.")
    
    elif "inventory" in userinput:
        print("Inventory:")
        for i in inventory:
            print(f"\t{i}")
            
    elif "use" in userinput:
        if "hammer" in userinput and "hammer" in inventory:
            use("hammer")
        elif "chain cutters" in userinput and "chain cutters" in inventory:
            use("chain cutters")
        elif "key" in userinput and "key" in inventory:
            use("key")
        elif "card" in userinput and "card" in inventory:
            use("card")
        else:
            print("Invalid item.")
    
    elif "password" in userinput:
        if "lol" in userinput:
            passwordScene()
        else:
            print("Incorrect password.")
            
    elif "remove" in userinput:
        if "hammer" in userinput and "hammer" in inventory:
            remove("hammer")
        elif "chain cutters" in userinput and "chain cutters" in inventory:
            remove("chain cutters")
        elif "key" in userinput and "key" in inventory:
            remove("key")
        elif "card" in userinput and "card" in inventory:
            remove("card")
        else:
            print("Invalid item.")
            
    elif "quit" in userinput:
        quitScene()
        
    else:
        print("What?")