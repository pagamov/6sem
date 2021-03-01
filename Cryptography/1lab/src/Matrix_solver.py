import copy
from time import time
import numpy as np
from color import color
from data import n
from lib import GCD
from gaus_solve_py import gaus_solve
import decimal

class Matrix_solver:
    def __init__(self, primes):
        self.matrix = []
        self.primes = primes
        self.gaus = []

        self.num_smooth_numbers = 0

        self.matrix = np.zeros((len(primes), len(primes)), dtype='uint8')
        # for i in range(len(primes)):
        #     self.matrix.append([])

    def add(self, smooth_number):
        if(self.num_smooth_numbers == len(self.primes)):
            return False
        self.matrix[:,self.num_smooth_numbers] = smooth_number
        self.num_smooth_numbers += 1
        # for i in range(len(self.primes)):
        #     self.matrix[i].append(smooth_number[i])

    def solve(self,smooth_numbers):
        # c++ matrix solve

        t = time()

        ans = [None,None]
        # lineal_rows = gaus_solve(self.gaus)
        lineal_rows = gaus_solve(self.matrix)

        print("\ndone solving matrix in",color(round(time() - t,4),'time'))
        t = time()

            
        for zero_column in range(len(lineal_rows[0])):

            t1 = time()

            print("\nfind",color("posible",'data'),"ans")
            b = [] #indexes of smooth numbers i guess
            for i in range(len(lineal_rows)):
                if lineal_rows[i][zero_column]:
                    b.append(i)
            # got vector b as indexes of posible ans

            print("\nseg1",color(round(time() - t1,4),'time'))
            t1 = time()

            left = 1
            right = []
            for i in b:
                left *= int(decimal.Decimal(n).sqrt() + 1) + smooth_numbers[i][0]
                right.append(smooth_numbers[i][2])
            true_right = int(1)

            right_piv = np.zeros(len(self.primes), int)
            # right_piv = [0] * len(self.primes)

            print("\nseg2",color(round(time() - t1,4),'time'))
            t1 = time()

            print(len(right), right[0][0])
            for r in right:
                right_piv += r
            
            print("\nseg3",color(round(time() - t1,4),'time'))
            t1 = time()

            for j in range(len(right_piv)):
                right_piv[j] //= 2

            print("\nseg4",color(round(time() - t1,4),'time'))
            t1 = time()
            
            for j in range(len(right_piv)):
                true_right *= pow(self.primes[j], int(right_piv[j]))

            print("\nseg5",color(round(time() - t1,4),'time'))
            t1 = time()

            gcd = min(GCD(abs(int(left+true_right)), n), GCD(abs(int(left-true_right)), n))
            if gcd > 1 and n // gcd * gcd == n:
                print("\nseg6",color(round(time() - t1,4),'time'))
                print(color("Solve Done",'strong'))
                ans = [gcd, n//gcd]
                break
            else:
                print("\nseg6",color(round(time() - t1,4),'time'))
                print("guess was",color('wrong', 'strong'),"keep search!\n")
                
            
        
        print("\ndone searching ans's",color(round(time() - t,4),'time'))
        return ans
