import copy
from time import time
import numpy as np
from color import color

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

    def solve(self):
        t = time()

        self.gaus = np.zeros((len(self.primes), len(self.primes)), 'int8')

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
        self.gaus = self.gaus % 2



        print(len(self.primes) - N, "rows and colums were deleted")
        print("form matrix",color(N,'data'),'x',color(N,'data'), end=" ")
        print("in",color(round(time() - t,4),'time'))
        if len(self.gaus[0]) == 0:
            return None


        # NOTE: solve
        t = time()

        lineal_rows =  np.zeros((len(self.gaus[0]), len(self.gaus[0])), 'int8')
        np.fill_diagonal(lineal_rows, 1)
        banned_rows = set()
        banned_numbers = set()

        t_find_row_total = 0
        t_add_columns_total = 0
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
                break

        print("\ndone operations",color(round(time() - t,4),'time'))

        t = time()
        b = []
        for i in range(len(lineal_rows)):
            if lineal_rows[i][zero_column]:
                b.append(i)
        return b

        print("form ans",color(round(time() - t,4),'time'))
        print("got",color(len(ans),'data')+" ans")
        return ans
