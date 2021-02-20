from multiprocessing import Pool
from time import time
import decimal,copy
from Primes import Primes
from Matrix_solver import Matrix_solver
from lib import GCD,Q,smooth_region,eratosthenes

class MPsieve:
    def __init__(self, q, primes):
        self.q = q
        self.primes = primes

    def __call__(self, L):
        return smooth_region(L[0],L[1],self.q,self.primes)

n = 104729 * 103591
B = 10**5

q = Q(n)
primes = Primes(n,B,q)
mpsieve = MPsieve(q,primes)

# print(len(mpsieve([0,10000])))
# exit()

reg = [[0,10000],
       [10000,20000],
       [20000,30000],
       [30000,40000],
       [40000,50000],
       [50000,60000]]

if __name__ == '__main__':
    t = time()
    for r in reg:
        smooth_region(r[0],r[1],q,primes)
    print("\ntime:",time()-t)

    t = time()
    with Pool(6) as p:
        ans = p.map(mpsieve, reg)
        print(len(ans))
    print("\ntime:",time()-t)
