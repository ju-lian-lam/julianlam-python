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