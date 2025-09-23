def question1()->None:
    list = []
    total = 0
    for i in range(6):
        number = int(input("Enter the number: "))
        list.append(number)
    # end for
    list.reverse()
    print(*list)
    for i in range(len(list)):
        total = total + list[i]
    # end for
    print(total)
    average = total / len(list)
    print(average)
# end procedure

def question2()->None:
    studentlist = ["name1", "ID1", "name2", "ID2", "name3", None, "name4", "ID4"]
    listlength = len(studentlist)
    name = input("Enter the student name: ")
    found = False
    for i in range(listlength):
        if (studentlist[i] == name):
            found = True
            print(f'Name found at position: {i+1}')
            if(studentlist[i+1] != None):
                print(f'Record number: {studentlist[i+1]}')
            break
        # end if
    # end for
    if (found == False):
        print("Name does not exist.")
    # end if
# end procedure

def question3()->None:
    Outlet1Sales = [10, 12, 15, 10]
    Outlet2Sales = [5, 8, 3, 6]
    Outlet3Sales = [10, 12, 15, 10]
    print(f'Total for Quarter One: {Outlet1Sales[0] + Outlet2Sales[0] + Outlet3Sales[0]}')
    print(f'Total for Quarter Two: {Outlet1Sales[1] + Outlet2Sales[1] + Outlet3Sales[1]}')
    print(f'Total for Quarter Three: {Outlet1Sales[2] + Outlet2Sales[2] + Outlet3Sales[2]}')
    print(f'Total for Quarter Four: {Outlet1Sales[3] + Outlet2Sales[3] + Outlet3Sales[3]}')
# end procedure

def question4()->None:
    total = [0, 0, 0, 0]
    outletSales = [[5,8,10,12],[2,4,6,8],[3,5,8,2],[6,7,4,2]]
    for outlet in range(4):
        for quarter in range(4):
            total[quarter] = total[quarter] + outletSales[outlet][quarter]
        # end for
    # end for
    for i in range(4):
        count = 1
        print(f'Total for quarter {i+1}: {total[i]}')
    # end for
# end procedure

def question5()->None:
    line = ""
    grid = [["O ","x ","x ","x "],["x ","x ","x ","x "],["x ","x ","x ","x "],["x ","x ","x ","x "],["x ","x ","x ","x "],["x ","x ","x ","x "]]
    print("Current Grid: ")
    for i in range(6):
        for z in range(4):
            line = line + grid[i][z]
        print(line)
        line = ""
        # end for
    # end for
    newrow = int(input())
    newcol = int(input())
    grid[newrow-1][newcol-1] = "O "
    grid[0][0] = "x "
    for i in range(6):
        for z in range(4):
            line = line + grid[i][z]
        print(line)
        line = ""
        # end for
    # end for
# end procedure

def question6()->None:
    carparkgrid = [["empty" for r in range(10) for c in range (6)]]
    print(carparkgrid)
    print("1. Reset all spaces in the car park to 'empty'")
    print("2. Park a car")
    print("3. Remove a car")
    print("4. Display the car park grid")
    print("5. Quit\n")
    option = int(input())
    while(option != 5):
        if (option == 1):
            carparkgrid = [["empty" for r in range(10) for c in range (6)]]
        elif (option == 2):
            registration = input()
            while True:
                row = int(input())
                col = int(input())
                if (carparkgrid[row][col] == "empty"):
                    carparkgrid[row][col] = registration
                    break
                else:
                    print("Already being used, please re-enter: ")
                # end if
            # end while
        elif (option == 3):
            registration = input()
            for r in range(10):
                for c in range(6):
                    if (carparkgrid[r][c] == registration):
                        carparkgrid[r][c] = "empty"
                    # end if
                # end for
            # end for
        elif (option == 4):
            print(carparkgrid)
        else:
            option = input("Invalid choice - please re-enter: ")
        # end if
        print("1. Reset all spaces in the car park to 'empty'")
        print("2. Park a car")
        print("3. Remove a car")
        print("4. Display the car park grid")
        print("5. Quit\n")
    # end while
    print("Goodbye")
# end procedure

