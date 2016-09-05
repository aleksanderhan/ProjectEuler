from time import time
from fastfibonacci import fibonacci
from fibonacci import fib1


n = 1e5
t1 = time()
print fibonacci(n)
t2 = time()
print fib1(n)
t3 = time()
print
print t2-t1
print t3-t2
