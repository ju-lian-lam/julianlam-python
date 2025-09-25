def question2()->None:
    students = ["studentno1", "studentno2", "studentno3", "studentno4", "studentno5", "studentno6", "studentno7", "studentno8", "studentno9", "studentno10", "studentno11", "studentno12", "studentno13", "studentno14", "studentno15", "studentno16", "studentno17", "studentno18", "studentno19", "studentno20"]
    print("GROUP 1: ")
    for i in range(0,20,2):
        print(students[i])
    # end for
    print("GROUP 2: ")
    for i in range(1,21,2):
        print(students[i])
    # end for
# end procedure

def question3()->None:
    school = ["AAAA", "BBBB", "CCCC", "DDDD"]
    medals = [4, 7, 1, 3]
    result = int(input("Enter the result: "))
    schoolNumber = int(input("Enter the school number: "))
    while True:
        if (schoolNumber == 1):
            medals[0] = medals[0] + result
        elif (schoolNumber == 2):
            medals[1] = medals[1] + result
        elif (schoolNumber == 3):
            medals[2] = medals[2] + result
        elif (schoolNumber == 4):
            medals[3] = medals[3] + result
        elif (schoolNumber == -1):
            for i in range(0,4):
                print(f'School number: {i+1}   School name: {school[i]}    Number of medals: {medals[i]}')
            break
            # end
        # end if
        result = int(input("Enter the result: "))
        schoolNumber = int(input("Enter the school number: "))
    # end while
# end procedure

