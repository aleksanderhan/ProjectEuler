'''
from is_prime import is_prime

def primeFactorList(n):
    primeList = []
    i = 2
    while i <= int(n*0.5) +2:
        if isPrime(i) and n%i == 0:
            primeList.append(i)
        i += 1
    return primeList


def powersOfPrimes(n, prime):
    powers = 0
    while n%prime == 0:
        powers += 1
        n = n/prime
    return powers


t = 1
i = 1
d = 1
while d <= 500:
    t = t + i + 1
    i += 1
    primes = primeFactorList(t)
    d = 1
    for prime in primes:
        d = d*(powersOfPrimes(t, prime) + 1)
  
print(t)
'''  


def NOD(n):
    nod = 0
    sqrt = int(n**0.5)
    for i in range(1, sqrt+1):
        if n%i == 0:
            nod += 2
        if sqrt*sqrt == n:
            nod -= 1
    return nod


t = 1
i = 1
while NOD(t) < 500:
    t = t + i + 1
    i += 1
print(t)

























