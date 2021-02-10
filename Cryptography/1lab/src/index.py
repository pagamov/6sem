from math import *
from random import randint
# n = 160769357899975610828199539114109518167531134514190990785144666932076614717841

# NOTE: 497293 = 509 * 977 primes
n = 497293



# NOTE 1: pick d >= 3
d = 3

# NOTE 2.1: get m : [n^(1/(d+1))] < m < [n^(1/d)]
low_bound = floor(n**((d+1)**-1))
print "low", int(low_bound)

up_bound = floor(n**(d**-1))
print "up", int(up_bound)

m = randint(low_bound, up_bound)
print "base", m

# NOTE 2.2: make polinome from n on m base : 123,2 -> {1, 1, 1, 1, 0, 1, 1}
def make_polinome(n, m):
    res = []
    piv = 0
    while n > m:
        piv = n / m
        res.append(n - piv * m)
        n = piv
    res.append(piv)
    return res

polinome = make_polinome(n,m)

print polinome

# NOTE 3: make f_1(x) = x^d + a_{d-1}x^(d-1) + ... + a_0
class f_1:
    def __init__(self,polinome):
        # self.m = m
        self.polinome = []
        for number in polinome:
            self.polinome.append(number)

    def __call__(self,x):
        res = 0
        i = 0
        for number in self.polinome:
            res += number * (x**i)
            i += 1
        return res


f1 = f_1(polinome)

# NOTE 4: make F_1(a,b) = b^d * f_1(a/b)
class F_1(f_1):
    def __call__(self,a,b):
        res = 0
        i = 0
        j = d
        for number in self.polinome:
            res += number * (a**i) * (b**j)
            i += 1
            j -= 1
        return res

F1 = F_1(polinome)

# NOTE 5.1: f_2(x) = x - m
class f_2:
    def __call__(self,x):
        return x - m

f2 = f_2()

# NOTE 5.2: F_2(a,b) = a - bm
class F_2:
    def __call__(self,a,b):
        return a - b*m

F2 = F_2()

# NOTE 6: pick L_1 and L_2 as sieve region : SR = {1 <= b <= L_1, -L_2 <= a <= L_2}
L1 = randint(m**(1/2),m)
L2 = randint(m**(1/2),m)

print "L1", L1
print "L2", L2
