import decimal,copy
from math import log10
from time import time

def GCD(m,n):
    mult = 1
    while True:
        if m == 0 or n == 0 or m == n:
            return mult*max(n,m)
        if m == 1 or n == 1:
            return mult*1
        if m % 2 == 0 and n % 2 == 0:
            mult *= 2
            m = m/2
            n = n/2
        if m % 2 == 0 and n % 2 != 0:
            m = m/2
        if m % 2 != 0 and n % 2 == 0:
            n = n/2
        if m % 2 != 0 and n % 2 != 0:
            if n > m:
                piv = (n-m)/2
                n = m
                m = piv
            elif n < m:
                m = (m-n)/2

# def jacobi(n, m):
#     j = 1
#     # rule 5
#     n %= m
#     while n:
#         # rules 3 and 4
#         t = 0
#         while not int(n) & 1:
#             n /= 2
#             t += 1
#         if t&1 and m%8 in (3, 5):
#             j = -j
#         # rule 6
#         if (n % 4 == m % 4 == 3):
#             j = -j
#         # rules 5 and 6
#         n, m = m % n, n
#     return j if m == 1 else 0

# def Legandr(a,p):
#     print("a",a)
#     print("p",p)
#     if a % p == 0:
#         return 0
#     if a < 0:
#         if abs((p-1)/2)%2 == 1:
#             return -1*Legandr(-a,p)
#         return Legandr(-a,p)
#     a %= p
#     print("a%p",a)
#     # primes = eratosthenes(long(sqrt(a)) + 1)
#     primes = eratosthenes(a)
#     k = [0] * len(primes)
#     i = 0
#     print(primes)
#     while a != 1 and i < len(primes):
#         if a % primes[i] == 0:
#             k[i] += 1
#             a /= primes[i]
#         else:
#             i += 1
#     ans = 1
#     print(k)
#     print("")
#     for i in range(len(k)):
#         if k[i] != 0 and k[i] % 2 != 0:
#             if primes[i] == 2:
#                 if abs(p%8) == 3:
#                     ans *= -1
#             else:
#                 ans *= Legandr(p,primes[i])
#                 if abs(((p-1)*(primes[i]-1)/4))%2 == 1:
#                     ans *= -1
#     return ans

def eratosthenes(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    return list(filter(lambda x: x != 0, numbers))

# def smooth_under(number, primes):
#     res = [0] * len(primes)
#     i = 0
#     flag = False
#     while abs(number) > 1 and i < len(primes):
#         if number % primes[i] == 0:
#             flag = True
#             res[i] += 1
#             number = number / primes[i]
#         else:
#             i += 1
#     if abs(number) != 1 or flag == None:
#         return None
#         # print "got one"
#     return res

# def perm_find(arr, pos):
#     if None not in arr:
#         return [arr]
#     if len(arr) == pos:
#         # NOTE: end of arr
#         return None
#     if arr[pos] == None:
#         a = copy.copy(arr)
#         a[pos] = 0
#         b = copy.copy(arr)
#         b[pos] = 1
#         res1 = perm_find(a, pos+1)
#         res2 = perm_find(b, pos+1)
#         if res1 != None and res2 != None:
#             return res1 + res2
#         else:
#             return [a,b]
#     else:
#         return perm_find(arr, pos+1)

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

# def Tonelli_Shanks(a,p):
#     # not used
#     a%=p
#     p_1 = p
#     z=-1
#     for i in range(p):
#         if jacobi(i,p) == -1:
#             z = i
#     Q=0
#     w=0
#     S = 0
#     while p_1 % 2 == 0:
#         p_1 %= 2
#         s += 1
#     Q = p_1
#
#     c = z**Q
#     r = a*((Q+1)/2)
#     t = a**Q
#     M = S
#     while t % p != 1:
#         S_ = 0
#         while t**(2**S_) % p != 0:
#             S_ += 1
#         w = c**(2**(S-S_-1))
#         r *= w
#         t *= w**2
#         c = w**2
#         S = S_
#     return r

def smooth_region(L1, L2, q, primes):
    res = []
    for i in range(L1, L2):
        res.append([i, q(i), [0]*len(primes)])
    s = []
    # NOTE: match r1 and r2 to L1 L2 region
    for i in range(len(primes)):
        s.append([])
        if len(primes.r[i]) != 2:
            print(primes.p[i], primes.r[i])
            print("Error != 2")
            exit()
        for r in primes.r[i]:
            k = int(L1 / primes(i))
            # print(primes(i))
            while r + k*primes(i) >= L1:
                k -= 1
            k+=1
            # if r + k*primes(i) < L1 or r + k*primes(i) >= L2:
            if r + k*primes(i) < L1:
                print("r:",r,"k:",k)
                print("p:",primes(i),r + k*primes(i))
                print("L1:",L1, "L2:",L2)
                print("Error s >= L2 s < L1")
                exit()
            s[i].append(r + k*primes(i))

    # sasha_loh = [0] * len(primes)
    for p in range(len(primes)):
        for s_i in s[p]:
            # print(s[p])
            for i in range(s_i, L2, primes(p)):
                # NOTE: find p^k < B and go for p^k
                while res[i - L1][1] % primes(p) == 0:
                    res[i - L1][1] /= primes(p)
                    res[i - L1][2][p] += 1
                # sasha_loh[p] += res[i - L1][2][p]
            # print "prime:", primes(p), "res:",sasha_loh[p]

    # for i in range(len(sasha_loh)):
    #     print "prime sr:", primes(i), "res sr:", sasha_loh[i] / (L2-L1)
    ans = []
    for i in range(len(res)):
        if abs(res[i][1]) == 1:
            ans.append([res[i][0],q(res[i][0]),res[i][2]])
    return ans
