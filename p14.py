def collatz(n, i = 1):
    while True:
        if n == 1:
            return i
        elif n%2 == 0:
            n = n//2
        elif n%2 == 1:
            n = 3*n + 1
        i += 1

print(collatz(13))

n = 0
a = 1
for i in range(1,1000000):
    if collatz(i) > n:
        n = collatz(i)
        a = i
print(a)
       

