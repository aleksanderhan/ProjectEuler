from gcd import gcd


#http://en.wikipedia.org/wiki/Formula_for_primes#Recurrence_relation
def generate_primes(N): 
	p = []
	a = 7
	n = 1
	while len(p) < N:
		an = a + gcd(n, a)
		print an
		diff = an-a
		if diff != 1:
			p.append(diff)
		a = an
		n += 1
	return p


'''
N = 10
primes = generate_primes(N)
print primes
from is_prime import is_prime
for p in primes:
	print is_prime(p)
'''