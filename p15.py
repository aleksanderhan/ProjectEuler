def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


n = 20
print factorial(2*n)/(2*factorial(n))


