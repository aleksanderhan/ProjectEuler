# Løsning basert på gradient decent
from numpy import *


def f(k, n):
    f = e**(k/n) - 1
    return f


def E(X, n):
    return abs(f(X[0], n) + f(X[1], n) + f(X[2], n) + f(X[3], n) - pi)

'''
def E_grad(X, n):
    s = sign(f(X[0], n) + f(X[1], n) + f(X[2], n) + f(X[3], n) - pi)
    pDE_a = (s*e**(X[0]/n)/n)
    pDE_b = (s*e**(X[1]/n)/n)
    pDE_c = (s*e**(X[2]/n)/n)
    pDE_d = (s*e**(X[3]/n)/n)
    return array([pDE_a, pDE_b, pDE_c, pDE_d])
'''
def E_grad(X, n):
    h = 1
    x1 = (f(X[0]+h, n) - f(X[0]-h, n))/(2*h)
    x2 = (f(X[1]+h, n) - f(X[1]-h, n))/(2*h)
    x3 = (f(X[2]+h, n) - f(X[2]-h, n))/(2*h)
    x4 = (f(X[3]+h, n) - f(X[3]-h, n))/(2*h)
    return array([x1, x2, x3, x4])


def norm(X):
    return sqrt(X[0]**2 + X[1]**2 + X[2]**2 + X[3]**2)


n = 200
gamma = 10
Xold = array([1, 2, 3, 4])
Xnew = array([1, 2, 3, 4])
while E(Xold, n) > 0.000001:
    Xold = Xnew
    Xnew = Xold - gamma*E_grad(Xold, n)
    print(Xnew)
print(Xnew)

#print(E_grad(array([1, 1, 900, 1]), 200))


'''
i = 4
for a in range(i):
    for b in range(i):
        for c in range(i):
            for d in range(i):
                print(a, b, c, d)
                print(E(array([a, b, c, d]), 200))
                print()
'''









    
