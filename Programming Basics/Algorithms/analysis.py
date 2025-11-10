import time

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative Fibonacci
def fibonacci_iterative(n):
    fib_numbers = [0, 1]
    for i in range(2, n + 1):
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
    return fib_numbers[n]

# Function to time a function call
def time_function(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return (end - start) * 1000, result  # return time in milliseconds

# Values of n to test
test_values = [10, 20, 25, 30, 35, 40]

print(f"{'n':<5}{'Recursive Time (ms)':<25}{'Iterative Time (ms)':<25}")
print("-" * 55)

for n in test_values:
    try:
        rec_time, rec_result = time_function(fibonacci_recursive, n)
    except RecursionError:
        rec_time = float('inf')
        rec_result = 'N/A'
    it_time, it_result = time_function(fibonacci_iterative, n)

    print(f"{n:<5}{rec_time:<25.2f}{it_time:<25.2f}")

# Optional: test very large n for iterative only
large_n = 100
it_time_large, _ = time_function(fibonacci_iterative, large_n)
print(f"\nIterative time for n={large_n}: {it_time_large:.2f} ms")
