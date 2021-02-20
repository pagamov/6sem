import copy
from time import time
import numpy as np

class Matrix_solver:
    def __init__(self, primes):
        self.matrix = []
        self.primes = primes
        self.gaus = []
        for i in range(len(primes)):
            self.matrix.append([])

    def add(self, smooth_number):
        for i in range(len(self.primes)):
            self.matrix[i].append(smooth_number[i])

    def solve(self):
        self.gaus = []
        t = time()
        for i in range(len(self.primes)):
            flag = False
            for j in self.matrix[i]:
                if j != 0:
                    flag = True
            if flag:
                self.gaus.append(copy.copy(self.matrix[i]))
        for i in range(len(self.gaus)):
            for j in range(len(self.gaus[i])):
                self.gaus[i][j] = self.gaus[i][j] % 2

        print("form matrix \033[95m"+str(len(self.gaus))+"\033[0m x \033[95m"+str(len(self.gaus[0]))+'\033[0m', "in time: " + '\033[96m' + str(round(time() - t,4)) + '\033[0m' + " sec")
        if len(self.gaus[0]) == 0:
            return None
        # NOTE: solve
        t = time()
        self.gaus = np.array(self.gaus, dtype=bool)
        lineal_rows =  np.zeros((len(self.gaus[0]), len(self.gaus[0])), bool)
        np.fill_diagonal(lineal_rows, True)
        banned_rows = set()
        banned_numbers = set()
        for y in range(len(self.gaus[0])):
            print("\rmult matrix " + '\033[92m' + str(round(float(y)/float(len(self.gaus[0]))*100,2))+"\033[0m %",end="")
            x = -1
            for i in range(len(self.gaus)):
                if self.gaus[i][y] == 1 and i not in banned_rows:
                    x = i
                    banned_rows.add(i)
                    banned_numbers.add(y)
                    break
            if x >= 0:
                for j in range(len(self.gaus[0])):
                    if j != y and self.gaus[x][j] == 1 and j not in banned_numbers:
                        lineal_rows[:,j] ^= lineal_rows[:,y]
                        self.gaus[:,j] ^= self.gaus[:,y]
                        # for i in range(len(self.gaus)):
                        #     self.gaus[i][j] = self.gaus[i][j] ^ self.gaus[i][y]
        print("\ndone operations \033[96m"+str(round(time() - t,4))+"\033[0m sec")
        t = time()
        ans = []
        for y in range(len(self.gaus[0])):
            if y not in banned_numbers:
                flag = True
                for x in range(len(self.gaus)):
                    if self.gaus[x][y] == 1:
                        flag = False
                        break
                if flag:
                    b = []
                    for i in range(len(lineal_rows)):
                        if lineal_rows[i][y]:
                            b.append(i)
                    ans.append(b)

        print("form ans \033[96m"+str(round(time() - t,4))+"\033[0m sec")
        print("got \033[95m"+str(len(ans))+"\033[0m ans")
        return ans
