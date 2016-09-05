from is_prime import is_prime

def prime_factors(n):   
    primes = []
    while n != 1:
        for i in range(2, n+1):
            if is_prime(i) and n%i == 0:
                primes.append(i)
                n = n//i
    return primes


f = []
i = 20
while i > 1:
    a = prime_factors(i)
    for j in a:
        if f.count(j) < a.count(j):
            f += [j]*(a.count(j)-f.count(j))
    i -= 1


p = 1
for i in f:
    p *= i
print(p)



