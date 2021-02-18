import copy
class Matrix_solver:
    def __init__(self, primes):
        # NOTE: matrix for storage i:primes j:x1,x2,x3,...,xn
        self.matrix = []
        self.primes = primes.p
        self.gaus = []
        # NOTE: DO NOT TAKE attempts to solve cases we alredy solve!
        # self.ban = [[]]
        for i in range(len(primes)):
            self.matrix.append([])

    def add(self, smooth_number):
        for i in range(len(self.primes)):
            self.matrix[i].append(smooth_number[i])
        # for i in range(len(self.ban)):
        #     self.ban[i].append(0)

    def log(self):
        print "matrix:"
        for i in range(len(self.primes)):
            print self.matrix[i]
        # print "ban list:"
        # for i in range(len(self.ban)):
        #     print self.ban[i]

    # def update_ban(self, ban_list):
    #     for i in range(len(ban_list)):
    #         self.ban.append(ban_list[i])

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
        banned_rows = []
        for j in range(len(self.gaus[0])):
            # print "new j"
            curr = -1
            for i in range(len(self.gaus)):
                if self.gaus[i][j] == 1 and i not in banned_rows:
                    curr = i
                    banned_rows.append(i)
                    break
            if curr >= 0:
                for i in range(len(self.gaus)):
                    if i != curr and self.gaus[i][j] == 1:
                        # print "summ", curr, "and", i
                        for sum in range(j, len(self.gaus[0])):
                            self.gaus[i][sum] = (self.gaus[i][sum] + self.gaus[curr][sum]) % 2
            # self.log()
        res = [None] * len(self.gaus[0])
        for i in range(len(self.gaus)):
            ones_in = 0
            indexes = []
            for j in range(len(self.gaus[0])):
                if self.gaus[i][j] == 1:
                    ones_in += 1
                    indexes.append(j)
            if ones_in == 1:
                res[indexes[0]] = 0
        # delete later
        return res
        piv = perm_find(res,0)
        res = []
        for solve in piv:
            if solve not in ban:
                res.append(copy.copy(solve))
        return res
