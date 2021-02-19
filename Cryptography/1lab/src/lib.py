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
    res = []
    for i in range(L1, L2):
        res.append([i, q(i), [0]*len(primes)])
    s = []
    primes_skipped = 0
    # NOTE: match r1 and r2 to L1 L2 region
    for i in range(len(primes)):
        s.append([])
        if len(primes.r[i]) != 2:
            print(primes.p[i], primes.r[i])
            print("Error != 2")
            exit()
        for r in primes.r[i]:
            k = int(L1 / primes(i))
            while r + k*primes(i) >= L1:
                k -= 1
            k+=1
            if r + k*primes(i) >= L2:
                primes_skipped += 1
            if r + k*primes(i) < L1:
                print("r:",r,"k:",k)
                print("p:",primes(i),r + k*primes(i))
                print("L1:",L1, "L2:",L2)
                print("Error s >= L2 s < L1")
                exit()
            s[i].append(r + k*primes(i))
    for p in range(len(primes)):
        for s_i in s[p]:
            for i in range(s_i, L2, primes(p)):
                # NOTE: find p^k < B and go for p^k
                while res[i - L1][1] % primes(p) == 0:
                    res[i - L1][1] /= primes(p)
                    res[i - L1][2][p] += 1
    ans = []
    for i in range(len(res)):
        if abs(res[i][1]) == 1:
            ans.append([res[i][0],q(res[i][0]),res[i][2]])

    print('\033[95m'+str(len(ans))+"\033[0m in ["+str(L1)+"..."+str(L2)+"] in time: " +'\033[96m'+ str(round(time() - t,4))+'\033[0m' + " sec","primes skipped: \033[95m"+str(round(primes_skipped/(2*len(primes))*100,2))+"\033[0m %")
    return ans
