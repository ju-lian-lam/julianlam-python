def method1():
    age = int(input("Enter an age: "))
    if (age > 11 and age <= 18):
        print("Age is:", 18)
    else:
        while (age <= 11 or age > 18):
            age = int(input("Enter an age: "))
        print("Age is:", 18)

def method2():
    age = 0
    while (age <= 11 or age > 18):
        age = int(input("Enter an age: "))
    print("Age is:", age)

gravity = 10

def printGravity():
    print(gravity)

def updateGravity(n):
    gravity = n

printGravity()
print(gravity)
updateGravity(5)
printGravity()