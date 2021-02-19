from lib import eratosthenes,jacobi,Q,tonelli
from time import time

class Primes:
    def __init__(self, n, B, q):
        primes = eratosthenes(B)
        self.p = []
        self.r = []
        q = Q(n)
        t = time()
        for i in range(1,len(primes)):
            print "\r", float(i)/float(len(primes))*100,"%",
            if jacobi(n%primes[i], primes[i]) == 1:
                t = tonelli(n,primes[i])
                r = [
                (t - q.m) % primes[i],
                (primes[i] - t - q.m) % primes[i]
                ]

                # r = []
                # j = 0
                # while j <= primes[i] and len(r) != 2:
                #     if q(j) % primes[i] == 0:
                #         # print primes[i], j, q(j)
                #         r.append(j)
                #     j += 1
                self.p.append(primes[i])
                self.r.append(r)

        print "\n",time() - t
        print "\nprimes done"

    def __call__(self,i):
        return self.p[i]
    def __len__(self):
        return len(self.p)
