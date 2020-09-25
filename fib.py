def fibonacci(n):
    fib = [0,1]+(n-2)*[None]
    for i in range(2,n):
        fib[i] = fib[i-1]+fib[i-2]
    return fib


x = fibonacci(10)

print(x)
