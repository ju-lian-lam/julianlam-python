def phelloWorld()->None:
    print("hello world")
# end procedure

def fhelloWorld()->str:
    return "hello, world"
# end function

#Main
if __name__ == "__main__":
    print("This is my basic library")
    phelloWorld()
    msg = fhelloWorld()
    print(msg)