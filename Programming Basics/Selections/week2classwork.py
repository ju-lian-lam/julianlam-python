def question2()->None:
    age = int(input("Enter an age: "))
    if (age > 10 and age < 19):
        print("Valid pupil age")
    else:
        print("Invalid input: enter a value from 11 to 18")
    # end if
# end function

def question3()->None:
    totalValue = float(input("Enter the total value of your order: "))
    ndDelivery = input("Do you want next day delivery? ")
    if (ndDelivery == "Yes"):
        print(f'Postage Charge: 5')
        print(f'Overall Charge: {totalValue + 5}')
    elif (ndDelivery == "No"):
        if (totalValue >= 15):
            print(f'Postage Charge: 0')
            print(f'Overall Charge: {totalValue}')
        elif (totalValue < 15):
            print(f'Postage Charge: 3.5')
            print(f'Overall Charge: {totalValue + 3.5}')
        # end if
    # end if
# end function

def question4()->None:
    Exam = int(input("Enter your exam score: "))
    Attendance = int(input("Enter your attendance: "))
    if (Attendance > 90):
        if (Exam > 90):
            print("Grade = A")
        elif (Exam > 80 and Exam <= 90):
            print("Grade = B")
        elif (Exam > 70 and Exam <= 80):
            print("Grade = C")
        elif (Exam <= 70):
            print("Fail")
        # end if
    else:
        print("Fail")
    # end if 
# end function

def question5p1()->None:
    movementGround = input("")
    movementFirst = input("")
    alarm = "OFF"
    if (alarm == "On"):
        if (movementGround == "True" and movementFirst == "True"):
            print("Intruder Alert")
            print("Intruder Alert")
        elif (movementGround == "True" and movementFirst == "False"):
            print("Intruder Alert")
        elif (movementGround == "False" and movementFirst == "True"):
            print("Intruder Alert")
        # end if
    # end if
# end function

def question5p2()->None:
    movementGround = input("")
    movementFirst = input("")
    alarm = "OFF"
    if (movementGround == "True" and movementFirst == "True"):
        alarm = "ON"
        print("Intruder Alert")
    elif (movementGround == "True" and movementFirst == "False"):
        alarm = "ON"
        print("Intruder Alert")
    elif (movementGround == "False" and movementFirst == "True"):
        alarm = "ON"
        print("Intruder Alert")
    # end if
# end function

def question6()->None:
    print("Car choices: ")
    print("1: Economy Car")
    print("2: Saloon Car")
    print("3: Sports Car")
    choice = input("")
    if (choice == "Economy Car" or choice == "Saloon Car" or choice == "Sports Car"):
        print("Valid Choice")
        final = input("Would you like to proceed or cancel?")
        print("Have a nice day.")
    else:
        print("Invalid Choice")
    # end if
# end function

def question7()->None:
    temp = input("Do you have a temperature?")
    if (temp == "Yes"):
        sore = input("Do you have a sore throat?")
        if (sore == "Yes"):
            print("You may have a throat infection.")
        elif (sore == "No"):
            cough = input("Do you have a cough?")
            if (cough == "Yes"):
                print("You have a chest infection.")
            elif (cough == "No"):
                print("You are diagnosed with a fever.")
            # end if
        # end if
    elif (temp == "No"):
        print("You're doing good.")
    # end if
# end function
