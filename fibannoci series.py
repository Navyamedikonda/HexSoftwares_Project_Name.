def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)
    
    return fib_sequence
n = int(input())
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence: [0]")
else:
    result = fibonacci(n)
    print(result)
