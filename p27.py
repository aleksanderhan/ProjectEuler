from isPrime import isPrime

'''
for n in range(40):
    p = n**2 + n + 41
    print(p, isPrime(p))

for n in range(80):
    p = n**2 - 79*n + 1601
    print(p, isPrime(p))
'''



A = 0
B = 0
N = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        p = n**2 + a*n + b
        while isPrime(p):
            n += 1
            p = n**2 + a*n + b
        if n > N:
            A = a
            B = b
            N = n

print(A*B)





        
