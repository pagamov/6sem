from lib import eratosthenes,Q,tonelli,legendre
from time import time
import numpy as np
import pickle
from data import B_search, B_file, B_save
from color import color

class Primes:
    def __init__(self, n, B, q):
        if B_search:
            # B_search == True so we need to find out factor base
            primes = eratosthenes(B)
            self.p = []
            self.r = []
            q = Q(n)
            t = time()

            if legendre(n%primes[0], primes[0]) == 1:
                tr = tonelli(n,primes[0])
                r = [(tr - q.m) % primes[0]]
                self.p.append(primes[0])
                self.r.append(r)

            # Для каждого прайма проверяем Лежандра и находим корни Тонелли Шенксом
            for i in range(1,len(primes)):
                print("\r"+color(round(float(i)/float(len(primes))*100,2),"%"),end="")
                if legendre(n%primes[i], primes[i]) == 1:
                    tr = tonelli(n,primes[i])
                    r = [(tr - q.m) % primes[i],(primes[i] - tr - q.m) % primes[i]]
                    self.p.append(primes[i])
                    self.r.append(r)

            print("\nprimes done in time: "+color(round(time() - t,4),"time"))
            print("primes len",color(len(self.p),"data"))

            if B_save:
                # we need to save our factor base in file B_file
                t = time()
                data = [B, n, self.p, self.r]
                with open(B_file, 'wb') as f:
                    pickle.dump(data, f)
                print("\nprimes saved in time: "+color(round(time() - t,4),"time"),"in file: "+str(B_file))
        else:
            # B_search == False so we need to upload factor base from B_file
            t = time()
            data = []
            with open(B_file, 'rb') as f:
                data = pickle.load(f)
            if data[0] != B:
                print(color("Primes::Error: wrong B!","strong"))
                exit()
            if data[1] != n:
                print(color("Primes::Error: wrong n!","strong"))
                exit()
            self.p = data[2]
            self.r = data[3]
            print(color("primes upload in time:","strong")+color(round(time() - t,4),"time"),"from file: "+str(B_file))
            print("primes len",color(len(self.p),"data"))

    def __getitem__(self,i):
        return self.p[i]
    def __len__(self):
        return len(self.p)
