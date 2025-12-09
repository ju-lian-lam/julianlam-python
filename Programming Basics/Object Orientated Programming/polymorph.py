class Foo:
    def __init__(self):
        self.__a = 0
    #end constructor

    def update(self):
        self.__a += 5
    #end procedure

    def getData(self):
        return self.__a
    #end function
#end class

class Baa:
    def __init__(self):
        self.__b = 0
    #end constructor

    def update(self):
        self.__b += 3
    #end procedure

    def getData(self):
        return self.__b
    #end function
#end class

obj_list = []
obj_list.append(Foo())
obj_list.append(Baa())

for obj in obj_list:
    obj.update()

for obj in obj_list:
    print(obj.getData())