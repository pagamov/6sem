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

        self.matrix = np.zeros((len(primes), len(primes)), dtype='int8')
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
        t = time()

        self.gaus = np.zeros((len(self.primes), len(self.primes)), int)

        N = 0
        for i in range(len(self.primes)):
            flag = False
            for j in self.matrix[i]:
                if j != 0:
                    flag = True
                    break
            if flag:
                self.gaus[N] = self.matrix[i]
                N += 1
                # self.gaus.append(list(self.matrix[i]))

        self.gaus = np.copy(self.gaus[:N,:N])

        print(color(len(self.primes) - N,'data'),"rows and colums were deleted")
        print("form matrix",color(N,'data'),'x',color(N,'data'), end=" ")
        print("in",color(round(time() - t,4),'time'))
        if len(self.gaus[0]) == 0:
            return [None, None]

        # c++ matrix solve

        t = time()
        lineal_rows = gaus_solve(self.gaus)
            
        for zero_column in range(len(lineal_rows[0])):
            print("\nfind",color("posible",'data'),"ans")
            b = [] #indexes of smooth numbers i guess
            for i in range(len(lineal_rows)):
                if lineal_rows[i][zero_column]:
                    b.append(i)
            # got vector b as indexes of posible ans
            left = 1
            right = []
            for i in b:
                left *= int(decimal.Decimal(n).sqrt() + 1) + smooth_numbers[i][0]
                right.append(smooth_numbers[i][2])
            true_right = int(1)
            right_piv = [0] * len(self.primes)
            for r in right:
                for j in range(len(self.primes)):
                    right_piv[j] += int(r[j])
            for j in range(len(right_piv)):
                right_piv[j] //= 2
            for j in range(len(right_piv)):
                true_right *= int(self.primes[j]**right_piv[j])

            gcd = min(GCD(abs(int(left+true_right)), n), GCD(abs(int(left-true_right)), n))
            if gcd > 1 and n // gcd * gcd == n:
                print(color("Solve Done",'strong'))
                ans = [gcd, n//gcd]
                break
            else:
                print("guess was",color('wrong', 'strong'),"keep search!\n")
        
        print("\ndone operations",color(round(time() - t,4),'time'))
        return ans


        #python matrix solve
        self.gaus = self.gaus % 2

        # NOTE: solve
        t = time()

        lineal_rows =  np.zeros((len(self.gaus[0]), len(self.gaus[0])), 'int8')
        np.fill_diagonal(lineal_rows, 1)
        banned_rows = set()
        banned_numbers = set()

        ans = [None,None]
        for y in range(N):
            print("\rGaus progress:",color(round(float(y)/float(len(self.gaus[0]))*100,2),'%'),end="")
            x = -1

            for i in range(N):
                if self.gaus[i, y] == 1:
                    x = -2
                    if x not in banned_rows:
                        x = i
                        banned_rows.add(i)
                        banned_numbers.add(y)
                        break

            if x >= 0:
                for j in range(N):
                    if j != y and self.gaus[x, j] == 1 and j not in banned_numbers:
                        lineal_rows[:,j] ^= lineal_rows[:,y]
                        self.gaus[:,j] ^= self.gaus[:,y]

            elif x == -1:
                zero_column = y
                # we find zero column as y
                print("\nfind",color("posible",'data'),"ans")
                b = [] #indexes of smooth numbers i guess
                for i in range(len(lineal_rows)):
                    # print(lineal_rows[i][zero_column], end=' ')
                    if lineal_rows[i][zero_column]:
                        b.append(i)
                # got vector b as indexes of posible ans
                left = 1
                right = []
                for i in b:
                    left *= int(decimal.Decimal(n).sqrt() + 1) + smooth_numbers[i][0]
                    right.append(smooth_numbers[i][2])
                true_right = int(1)
                right_piv = [0] * len(self.primes)
                for r in right:
                    for j in range(len(self.primes)):
                        right_piv[j] += int(r[j])
                for j in range(len(right_piv)):
                    right_piv[j] //= 2
                for j in range(len(right_piv)):
                    true_right *= int(self.primes[j]**right_piv[j])

                gcd = min(GCD(abs(int(left+true_right)), n), GCD(abs(int(left-true_right)), n))
                if gcd > 1 and n // gcd * gcd == n:
                    print(color("Solve Done",'strong'))
                    ans = [gcd, n//gcd]
                    break
                else:
                    print("guess was",color('wrong', 'strong'),"keep search!\n")

        print("\ndone operations",color(round(time() - t,4),'time'))
        return ans
