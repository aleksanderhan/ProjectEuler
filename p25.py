n = 3
fib = [1, 1, 2]
while len(str(fib[2])) < 1000:
          fib[0] = fib[1]
          fib[1] = fib[2]
          fib[2] = fib[1] + fib[0]
          n += 1
          
print(n)
