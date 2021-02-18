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

def jacobi(n, m):
    j = 1
    # rule 5
    n %= m
    while n:
        # rules 3 and 4
        t = 0
        while not n & 1:
            n /= 2
            t += 1
        if t&1 and m%8 in (3, 5):
            j = -j
        # rule 6
        if (n % 4 == m % 4 == 3):
            j = -j
        # rules 5 and 6
        n, m = m % n, n
    return j if m == 1 else 0

def Legandr(a,p):
    print "a",a
    print "p",p
    if a % p == 0:
        return 0
    if a < 0:
        if abs((p-1)/2)%2 == 1:
            return -1*Legandr(-a,p)
        return Legandr(-a,p)
    a %= p
    print "a%p",a
    # primes = eratosthenes(long(sqrt(a)) + 1)
    primes = eratosthenes(a)
    k = [0] * len(primes)
    i = 0
    print primes
    while a != 1 and i < len(primes):
        if a % primes[i] == 0:
            k[i] += 1
            a /= primes[i]
        else:
            i += 1
    ans = 1
    print k
    print ""
    for i in range(len(k)):
        if k[i] != 0 and k[i] % 2 != 0:
            if primes[i] == 2:
                if abs(p%8) == 3:
                    ans *= -1
            else:
                ans *= Legandr(p,primes[i])
                if abs(((p-1)*(primes[i]-1)/4))%2 == 1:
                    ans *= -1
    return ans

def eratosthenes(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    return list(filter(lambda x: x != 0, numbers))
# rej = 0
# conf = 0
# real = 0
# glob_min = 10000
def smooth_under(number, primes):
    # print "\n", number, "\n", log10(number)
    # global rej, conf, real, glob_min
    # print "\r",rej, conf, real,
    # r = log10(abs(number))
    # for prime in primes:
    #     # if number % prime == 0:
    #     r -= log10(prime)
    # if abs(r) < glob_min:
    #     glob_min = abs(r)
    #     # print "\nmin",100*glob_min
    # if abs(r) > 5:
    #     rej += 1
    #     return None
    # conf += 1
    res = [0] * len(primes)
    i = 0
    flag = False
    while abs(number) > 1 and i < len(primes):
        if number % primes[i] == 0:
            flag = True
            res[i] += 1
            number = number / primes[i]
        else:
            i += 1
    if abs(number) != 1 or flag == None:
        return None
        # print "got one"
    return res

def perm_find(arr, pos):
    if None not in arr:
        return [arr]
    if len(arr) == pos:
        # NOTE: end of arr
        return None
    if arr[pos] == None:
        a = copy.copy(arr)
        a[pos] = 0
        b = copy.copy(arr)
        b[pos] = 1
        res1 = perm_find(a, pos+1)
        res2 = perm_find(b, pos+1)
        if res1 != None and res2 != None:
            return res1 + res2
        else:
            return [a,b]
    else:
        return perm_find(arr, pos+1)

class Q:
    def __init__(self,n):
        self.n = n
        self.m = long(decimal.Decimal(n).sqrt() + 1)
    def __call__(self,x):
        return (x + self.m)**2 - self.n

def Tonelli_Shanks(a,p):
    a%=p
    p_1 = p
    z
    for i in range(p):
        if jacobi(i,p) == -1:
            z = i
    Q,w
    S = 0
    while p_1 % 2 == 0:
        p_1 %= 2
        s += 1
    Q = p_1

    c = z**Q
    r = a*((Q+1)/2)
    t = a**Q
    M = S
    while t % p != 1:
        S_ = 0
        while t**(2**S_) % p != 0:
            S_ += 1
        w = c**(2**(S-S_-1))
        r *= w
        t *= w**2
        c = w**2
        S = S_
    return r

def smooth_region(L1, L2, q, primes):
    res = []
    for i in range(L1, L2):
        res.append([i, q(i), [0]*len(primes)])
    s = []
    # t = time()
    # for i in range(len(primes)):
    #     s.append([])
    #     # if jacobi()
    #     for j in range(L1, L1 + primes[i]):
    #         if q(j) % primes[i] == 0:
    #             s[i].append(j)
    #             if len(s[i]) == 2:
    #                 break
    # print "r",time() - t

    # NOTE: match r1 and r2 to L1 L2 region
    for i in range(len(primes)):
        s.append([])
        if len(primes.r[i]) != 2:
            print primes.p[i], primes.r[i]
            print "Error != 2"
            exit()
        for r in primes.r[i]:
            k = (L1) / primes(i)
            while r + k*primes(i) >= L1:
                k -= 1
            k+=1
            if r + k*primes(i) < L1:
                print r,k,primes(i),r + k*primes(i),L1
                print "Error < L1"
                exit()
            s[i].append(r + k*primes(i))

    for p in range(len(primes)):
        for s_i in s[p]:
            for i in range(s_i, L2, primes(p)):
                while res[i - L1][1] % primes(p) == 0:
                    res[i - L1][1] /= primes(p)
                    res[i - L1][2][p] += 1
    ans = []
    for i in range(len(res)):
        if abs(res[i][1]) == 1:
            ans.append([res[i][0],q(res[i][0]),res[i][2]])
    # for i in range(len(ans)):
    #     print ans[i]
    return ans