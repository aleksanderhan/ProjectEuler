from is_prime import is_prime

def largest_prime_factor(n):
    i = 2
    while i != n:
        if is_prime(i) and n%i == 0:
            n = int(n/i)
        else:
            i += 1
    return(i)


print(largest_prime_factor(600851475143))

