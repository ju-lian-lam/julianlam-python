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