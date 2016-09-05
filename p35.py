from is_prime import is_prime


primes = []
for p in range(1000001):
    if is_prime(p):
        primes.append(p)
        

def cycle(p):
    p=str(p)
    return int(p[-1] + p[:-1])


circularPrimes = []
for prime in primes:
    n = len(str(prime))
    circular = True
    for i in range(n-1):
        prime = cycle(prime)
        if prime not in primes:
            circular = False
    if circular:
        circularPrimes.append(prime)
        
print(len(circularPrimes))
