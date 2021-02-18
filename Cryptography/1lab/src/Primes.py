from lib import eratosthenes,jacobi,Q

class Primes:
    def __init__(self, n, B, q):
        primes = eratosthenes(B)
        self.p = []
        self.r = []
        q = Q(n)
        for i in range(1,len(primes)):
            print "\r", float(i)/float(len(primes))*100,"%",
            if jacobi(n%primes[i], primes[i]) == 1:
                r = []
                j = 0
                while j <= primes[i] and len(r) != 2:
                    if q(j) % primes[i] == 0:
                        r.append(j)
                    j += 1
                self.p.append(primes[i])
                self.r.append(r)
        print "\nprimes done"

    def __call__(self,i):
        return self.p[i]
    def __len__(self):
        return len(self.p)
