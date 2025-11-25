class OCR_Stack:
    def __init__(self,size):
        self.__MAXSIZE = size
        self.data = [None for _ in range(self.__MAXSIZE)]
        self.sp = -1
    #end procedure

    def __str__(self):
        # ANSI Colour Codes
        RED = "\033[31m"
        GREEN = "\033[32m"
        RESET = "\033[0m"

        rtn_str = ''

        for index in range(self.__MAXSIZE):
            item = self.data[index]

            if index <= self.sp:
                colour = GREEN    
            else:
                colour = RED     

            rtn_str = f"{item}\n" + rtn_str

        return rtn_str
    #end function

    def push(self,item):
        self.sp += 1
        self.data[self.sp] = item
        #end procedure

    def pop(self):
        if (self.sp == -1):
            return "List Empty"
        else:
            temp = self.data[self.sp]
            self.sp -= 1
            self.data[self.sp + 1] = None
            return temp
        #end if
    #end function

    def peek(self):
        return self.data[self.sp]
    #end function

    def size(self):
        counter = 0
        for count in range(self.__MAXSIZE):
            if (self.data[count] != None):
                counter += 1
            #end if
        return counter
        #end for
    #end function
#end class

my_stack = OCR_Stack(10)
print(my_stack)
"""Can you use the starter code to create  a OOP simulation of the OCR stack from the textbook. You will need to add the following methods: push,
 pop, peek and size. Update the __str__ method so that items in the stack are green, and any items above the stack pointer should be red."""