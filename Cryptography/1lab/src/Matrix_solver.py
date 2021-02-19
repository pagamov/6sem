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
            # self.matrix.append(np.array([]).astype(int))


    def add(self, smooth_number):
        for i in range(len(self.primes)):
            self.matrix[i].append(smooth_number[i])
            # self.matrix[i] = np.append(self.matrix[i],smooth_number[i])
    def log(self):
        print("matrix:")
        for i in range(len(self.primes)):
            print(self.matrix[i])

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
                # self.gaus.append(np.array(self.matrix[i]))
        for i in range(len(self.gaus)):
            for j in range(len(self.gaus[i])):
                self.gaus[i][j] = self.gaus[i][j] % 2

        print("form matrix", '\033[95m' + str(len(self.gaus)) + '\033[0m', "x", '\033[95m' + str(len(self.gaus[0])) + '\033[0m', "in time: " + '\033[96m' + str(time() - t) + '\033[0m' + "sec")
        # NOTE: solve
        if len(self.gaus[0]) == 0:
            return None

        t = time()
        lineal_rows = []
        for i in range(len(self.gaus[0])):
            lineal_rows.append({i})
        banned_rows = set()
        banned_numbers = set()
        for y in range(len(self.gaus[0])):
            print("\r"+"mult matrix " + '\033[92m' + str(round(float(y)/float(len(self.gaus[0]))*100))+"%"+'\033[0m',end="")
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
                        for elem in lineal_rows[y]:
                            if elem in lineal_rows[j]:
                                lineal_rows[j].remove(elem)
                            else:
                                lineal_rows[j].add(elem)
                        for i in range(len(self.gaus)):
                            self.gaus[i][j] = (self.gaus[i][j] + self.gaus[i][y]) % 2
        print("\ndone operations", '\033[96m' + str(time() - t) + "\033[0m"+" sec")
        t = time()

        ans = []
        for y in range(len(self.gaus[0])):
            flag = True
            for x in range(len(self.gaus)):
                if self.gaus[x][y] == 1:
                    flag = False
                    break
            if flag:
                if len(lineal_rows[y]) >= 2:
                    ans.append(lineal_rows[y])

        print("form ans", '\033[96m' + str(time() - t) + "\033[0m" + " sec")
        print("got " + '\033[95m' + str(len(ans)) +"\033[0m"+ " ans")
        return ans
