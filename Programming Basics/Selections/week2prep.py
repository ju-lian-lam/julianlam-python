def question1()->None:
    name = input("Enter your name: ")
    if (name == "Hazel"):
        print("Hello Hazel")
    else:
        print(f"We haven't met yet, {name}, pleased to meet you.")
    # end if
# end function

def question2()->None:
    temp = input("Enter the temperature: ")
    humidity = input("Enter the humidity: ")
    window = input("Enter the status of the window: ")
    if (window == "closed"):
        if (temp > 25 and humidity > 50):
            print("Open the window")
        # end if
    elif (window == "open"):
        if (temp < 10 and humidity < 50):
            print("Close the window")
        # end if
    # end if
# end function

def question4()->None:
    print("Select one of the following options: ")
    print("Enter A for Multiply: ")
    print("Enter B for Divide: ")
    print("Enter C for Add: ")
    print("Enter D for Subtract: ")
    print("Enter E for Remainder Division: ")
    option = input("Enter your option: ")
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    match option:
        case "A": print(num1 * num2)
        case "B": print(num1 / num2)
        case "C": print(num1 + num2)
        case "D": print(num1 - num2)
        case "E": print(num1 % num2)
    # end match
# end function

def question5()->None:
    year = int(input("Enter a year: "))
    leapYear = False
    if ((year % 4) == 0):
        leapYear = True
    elif ((year % 100) == 0):
        leapYear = False
    elif ((year % 400) == 0):
        leapYear = True
    # end if
    if (leapYear == True):
        print(f"{year} is a leap year.")
    elif (leapYear == False):
        print(f"{year} is not a leap year.")
    # end if
# end function