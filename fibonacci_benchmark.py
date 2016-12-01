from time import time
import fibonacci as pf
import cFibonacci as cf

n = 1000000
t1 = time()
pf.ifib(n)
t2 = time()
cf.ifib(n)
t3 = time()

print
print "n=" + str(n)
print "Iterative fibonacci time in Python: " + str(t2-t1)
print "Iterative fibonacci time in C: " + str(t3-t2)
print "C/Python ratio: " + str((t2-t1)/(t3-t2))

print
t1 = time()
pf.fdfib(n)
t2 = time()
print "Fast doubling fibonacci time in Python: " + str(t2-t1)

print
n = 40
t1 = time()
pf.rfib(n)
t2 = time()
cf.rfib(n)
t3 = time()
print "n=" + str(n)
print "Recursive fibonacci time in Python: " + str(t2-t1)
print "Recursive fibonacci time in C: " + str(t3-t2)
print "C/Python ratio: " + str((t2-t1)/(t3-t2))
