def question3()->None:
    print("1. Add name")
    print("2. Display list")
    print("3. Quit")
    print("")
    choice = int(input("Enter your choice: "))
    list = ["", "", "", "", "", "", "", "", "", ""]
    while (choice != 3):
        if (choice == 1):
            name = input("Enter the name to be added to the list")
            pos = int(input("Enter the position in the list to insert the name (1-10): "))
            list[pos-1] = (f'{pos} {name}')
        elif (choice == 2):
            print(*list)
        else:
            choice = int(input("Invalid choice - please re-enter: "))
        # end if
        print("1. Add name")
        print("2. Display list")
        print("3. Quit")
        print("")
        choice = int(input("Enter your choice: "))
    # end while
    if (choice == 3):
        print("")
        print("Program terminating")
    # end if
# end procedure     

question3()
