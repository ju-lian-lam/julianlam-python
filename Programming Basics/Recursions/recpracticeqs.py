def question1(n):
    if (n == 0):
        return 1
    else:
        return n * question1(n-1)

print(question1(6))

def question2(fib):
    if (fib <= 1):
        return fib
    else:
        return question2(fib-1) + question2(fib-2)

print(question2(10))

def question3(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + question3(nums[1:])

numbers = [10, 20, 30, 40]
print(question3(numbers))

def addEven(a,b):
    if (a > b):
        return 0
    elif (a % 2 == 0):
        return a + addEven(a+1, b)
    else:
        return addEven(a+1, b)

print(addEven(1,20))
