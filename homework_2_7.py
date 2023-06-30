def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
nineth = 9
for i in range(nineth):
    fibonacci(i)
print(fibonacci(8))
