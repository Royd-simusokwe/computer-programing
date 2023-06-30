def sum_digits(n):
    if n == 0:
        return 0
    return int(n%10) + sum_digits(n / 10)
    
n = int(input("your positive integer"))
sum = sum_digits(n)
print(sum)
    