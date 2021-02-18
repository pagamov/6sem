import copy
class Matrix_solver:
    def __init__(self, primes):
        # NOTE: matrix for storage i:primes j:x1,x2,x3,...,xn
        self.matrix = []
        self.primes = primes
        self.gaus = []
        # NOTE: DO NOT TAKE attempts to solve cases we alredy solve!
        for i in range(len(primes)):
            self.matrix.append([])

    def add(self, smooth_number):
        for i in range(len(self.primes)):
            self.matrix[i].append(smooth_number[i])

    def log(self):
        print "matrix:"
        for i in range(len(self.primes)):
            print self.matrix[i]

    def solve(self):
        # NOTE: make matrix for gaus and mod 2
        self.gaus = []
        # NOTE: cansel all p with 0 in them
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
        # NOTE: solve
        if len(self.gaus[0]) == 0:
            return None
        lineal_rows = []
        for i in range(len(self.gaus[0])):
            lineal_rows.append([i])
        banned_rows = []
        for y in range(len(self.gaus[0])):
            x = -1
            for i in range(len(self.gaus)):
                if self.gaus[i][y] == 1 and i not in banned_rows:
                    x = i
                    banned_rows.append(i)
                    break
            if x >= 0:
                for j in range(len(self.gaus[0])):
                    if j != y and self.gaus[x][j] == 1:
                        for elem in lineal_rows[y]:
                            if elem in lineal_rows[j]:
                                lineal_rows[j].remove(elem)
                            else:
                                lineal_rows[j].append(elem)
                        for i in range(len(self.gaus)):
                            self.gaus[i][j] = (self.gaus[i][j] + self.gaus[i][y]) % 2
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
        return ans
