def toBinary(number):
    remainder = []
    while (number > 0):
        store = number % 2
        number = number // 2
        remainder.append(store)
    remainder.reverse()
    return remainder

number = int(input())
while True:
    if (number >= 1 and number <= 255):
        break
    else:
        print("Error - Enter a number between 1 and 255: ")
        number = int(input())

list = toBinary(number)
for i in range(len(list)):
    print(list[i], end="")
    

