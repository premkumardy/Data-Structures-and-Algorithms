
count = 0

def Fibonacci(n):
    global count
    count += 1
    if n <= 1:
        return n

    return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(50))