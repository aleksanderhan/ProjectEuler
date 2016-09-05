fib = [1, 2]
fib_even = [2]
i = 2
while fib[i-1] + fib[i-2] <= 4000000:
    fib.append(fib[i-1] + fib[i-2])
    if fib[i]%2 == 0:
        fib_even.append(fib[i])
    i += 1
print(sum(fib_even))

