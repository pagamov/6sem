# -*- coding: utf-8 -*-
import decimal,copy
from color import color
from math import log10
from time import time
import numpy as np
from debug_info import smooth_region_output

def GCD(m,n):
    mult = 1
    while True:
        if m == 0 or n == 0 or m == n:
            return mult*max(n,m)
        if m == 1 or n == 1:
            return mult
        if m % 2 == 0 and n % 2 == 0:
            mult *= 2
            m = m//2
            n = n//2
        if m % 2 == 0 and n % 2 != 0:
            m = m//2
        if m % 2 != 0 and n % 2 == 0:
            n = n//2
        if m % 2 != 0 and n % 2 != 0:
            if n > m:
                piv = (n-m)//2
                n = m
                m = piv
            elif n < m:
                m = (m-n)//2

def eratosthenes(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    return list(filter(lambda x: x != 0, numbers))

class Q:
    def __init__(self,n):
        self.n = n
        self.m = int(decimal.Decimal(n).sqrt() + 1)
    def __call__(self,x):
        return (x + self.m)**2 - self.n

def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)

    z = 2
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r

def smooth_region(L1, L2, q, primes):
    t = time()
    # все значения между L1 и L2
    res0 = list(range(L1, L2))
    # единица означает что число под этим индексом гладкое
    res1 = [q(x) for x in range(L1, L2)]
    # массив из разложений чисел по простым
    res2 = np.zeros((len(res0), len(primes)), dtype="int8")
    table_creation_time = time() - t

    t = time()
    s = []
    primes_skipped = 0
    # подгоняем r до [L1, L2] => получаем s
    for i in range(len(primes)):
        # print("\rshift "+'\033[92m'+str(round(float(i)/float(len(primes))*100,2))+'\033[0m'+" %",end="")
        s.append([])
        for r in primes.r[i]:
            k = L1 // primes[i]
            while r + k*primes[i] >= L1:
                k -= 1
            k+=1
            if r + k*primes[i] >= L2:
                primes_skipped += 1
            s[i].append(r + k*primes[i])

    s_search_time = time() - t

    t = time()
    for p in range(len(primes)):
        # print("\rsuive "+'\033[92m'+str(round(float(p)/float(len(primes))*100,2))+'\033[0m'+" %",end="")
        for s_i in s[p]:
            if s_i < L2:
                res2[s_i - L1::primes[p], p] += 1
                for i in range(s_i, L2, primes[p]):
                    res1[i - L1] //= primes[p]
                for i in range(s_i, L2, primes[p]):
                    x = i - L1
                    while res1[x] % primes[p] == 0:
                        res1[x] //= primes[p]
                        res2[x, p] += 1

    prime_div_time = time() - t

    t = time()
    ans = []
    for i in range(len(res1)):
        if abs(res1[i]) == 1:
            ans.append([res0[i],q(res0[i]),np.copy(res2[i])])

    answer_fill_time = time() - t
    smooth_region_output(table_creation_time, s_search_time, prime_div_time,
                         answer_fill_time, ans, L1, L2, primes_skipped, primes)

    return ans


def get_region(idx, step):
    """
    return unique region for specified index
    if index is even: return positive
                 odd: return negative
    """
    # четные: положительный знак, нечетные: отрицательный
    sign = (idx % 2) * (-1)
    if sign == 0:
        return [idx * step, (idx + 1) * step]
    else:
        return [- (idx) * step, - (idx - 1) * step]
