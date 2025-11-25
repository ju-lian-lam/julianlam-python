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

class Puppy(Dog):
    def __init__(self, name, colour, shoesChewed):
        super().__init__(name, colour)
        self.__shoesChewed = shoesChewed
    #end constructor

    def bark(self, barkTimes):
        for _ in range(barkTimes):
            print("Yap!")
            #next _
    #end procedure 

    def setShoesChewed(self, shoesChewed):
        self.__shoesChewed = shoesChewed
    #end procedure

    def getShoesChewed(self):
        return self.__shoesChewed
    #end function
#end class 

myDog3 = Dog("Mutt", "Unknown")

if myDog3.getColour() == "Unknown":
    newColour = input("Please enter the dog's colour: ")
    myDog3.setColour(newColour)

print("Dog's name:", myDog3.getName())
print("Dog's colour:", myDog3.getColour())

myPuppy1 = Puppy("Rex", "Black", 3)
myPuppy2 = Puppy("Spot", "Brown", 5)

print("-------------------------")
print("Puppy's name:", myPuppy1.getName())
print("Puppy's colour:", myPuppy1.getColour())
print("Shoes chewed by puppy:", myPuppy1.getShoesChewed())

myPuppy1.bark(2)
myPuppy2.bark(3)
myDog3.bark(2)