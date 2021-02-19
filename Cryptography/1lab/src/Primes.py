from lib import eratosthenes,Q,tonelli,legendre
from time import time
import numpy as np

class Primes:
    def __init__(self, n, B, q):
        primes = eratosthenes(B)
        self.p = []
        self.r = []
        q = Q(n)
        t = time()
        for i in range(1,len(primes)):
            print("\r"+'\033[92m'+str(round(float(i)/float(len(primes))*100,2))+'\033[0m'+" %",end="")
            if legendre(n%primes[i], primes[i]) == 1:
            # if jacobi(n%primes[i], primes[i]) == 1:
                tr = tonelli(n,primes[i])
                r = [
                (tr - q.m) % primes[i],
                (primes[i] - tr - q.m) % primes[i]
                ]
                # print(r)

                # r = []
                # j = 0
                # while j <= primes[i] and len(r) != 2:
                #     if q(j) % primes[i] == 0:
                #         # print primes[i], j, q(j)
                #         r.append(j)
                #     j += 1
                self.p.append(primes[i])
                self.r.append(r)

        print("\nprimes done in time: "+ '\033[96m'+ str(round(time() - t,4))  + '\033[0m'+  " sec")
        print("primes len " + '\033[95m' + str(len(primes))+'\033[0m')

    def __call__(self,i):
        return self.p[i]
    def __len__(self):
        return len(self.p)
