numbers = [3, 6, 2, 8, 1]

def sum(numbers):
    total = 0
    for n in range (len(numbers)):
        total = total + numbers[n]
    return total

print(sum(numbers))

def recursionsum(arr):
    if (len(arr) == 1):
        return arr[0]
    else:
        return arr[0] + recursionsum(arr[1:])

print(recursionsum(numbers))

import time

def fib(n):
    if (n <= 1):
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    fibNumbers = [0,1]
    for i in range (2, n+1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])

    return fibNumbers[n]

starttime1 = time.time()
print(fib(10))
stoptime1 = time.time()
total = stoptime1 - starttime1
print(f'Total time using recursion, {total}s')

startime2 = time.time()
print(fib2(10))
stoptime2 = time.time()
total2 = stoptime2 - startime2
print(f'Total time using itertation {total2}s')