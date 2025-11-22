class Dog:
    def __init__(self, name, colour):
        self.__name = name
        self.__colour = colour
    #end constructor

    def bark(self, barkTimes):
        for _ in range(barkTimes):
            print("Woof!")
            #next _
    #end procedure

    def setColour(self, myColour):
        self.__colour = myColour
    #end procedure
    

    def getColour(self):
        return self.__colour
    #end function

    def getName(self):
        return self.__name
    #end function
#end class

myDog3 = Dog("Mutt", "Unknown")

if myDog3.getColour() == "Unknown":
    newColour = input("Please enter the dog's colour: ")
    myDog3.setColour(newColour)

print("Dog's name:", myDog3.getName())
print("Dog's colour:", myDog3.getColour())
