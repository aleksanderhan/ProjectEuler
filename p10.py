from is_prime import is_prime

sum_primes = 2
i = 1
while i < 2000000:
    if is_prime(i):
        sum_primes += i
    i += 2
print(sum_primes)
