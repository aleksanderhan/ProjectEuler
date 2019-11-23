from math import sqrt

#iterativ
def ifib(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        i = 2
        fp, fpp = 1, 1
        while i < n:
            f = fp + fpp
            fp, fpp = f, fp
            i += 1
        return f

# rekursiv
def rfib(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return rfib(n-1) + rfib(n-2)

# Fast doubling Fibonacci algorithm
def fdfib(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]

# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

# se side 59 i introduction to algorithms (algdat)
# avrundingsfeil for store n
def fib4(n):
    phi = (1+sqrt(5))/2
    return int((phi**n)/sqrt(5) + 0.5)



'''
from time import clock
n = 100000

t0=clock()
fib1(n)
t1 = clock()
fib2(n)
t2 = clock()
fib4(n)
t3 = clock()

print("fib1:", t1-t0)
print("fib2:", t2-t1)
print("fib4:", t3-t2)
'''
