map = [["r1,1","r1,2","r1,3"],["r2,1","r2,2","r2,3"],["r3,1","r3,2","r3,3"]]
winCondition = False
pos = map[1][1]
inventory = []

while (winCondition == False):
    choice = input("Enter a choice:")
    if (choice == "north"):
        print("You are in a forest. Paths lead east and west.")
        if (choice == "east"):
            print("You are in a castle hall. A guard blocks a door south.")
            choice = input("Enter a choice:")
            if (choice == "south"):
                print("You stare at the guard. The guard attacks you. Game over.")
            elif (choice == "east"):
                print("You are in a forest. Paths lead east and west.")
                continue
    elif (choice == "east"):
        print("You are at a river bank. The water flows swiftly.")
        print("There is a yew tree. Would you like to inspect it?")
        selection = input("Enter a choice:")
        if (selection == "yes"):
            print("You have found a key. It is now stored in your inventory")
            inventory.append("Key")
        elif (selection == "no"):
            choice == input("Where would you like to go now?")
            if (choice == "north"):
                print("You are in a forest. Paths lead east and west.")
                continue
            elif (choice == "south"):
                print("Locked as of currently.")
    elif (choice == "inventory"):
        print(inventory)
    elif (choice == "quit"):
        print("Thanks for playing.")
    else:
        print("Invalid command.")