class Gauss_Jordane:
    def __init__(self, data, primes):
        self.matrix = []
        self.primes = primes
        for i in range(len(primes)):
            flag = False
            for j in data.matrix[i]:
                if j != 0:
                    flag = True
            if flag:
                self.matrix.append(copy.copy(data.matrix[i]))

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] % 2

    def log(self):
        print("Gauss_Jordane matrix:")
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def solve(self, ban):
        if len(self.matrix[0]) == 0:
            return None
        banned_rows = []
        for j in range(len(self.matrix[0])):
            # print "new j"
            curr = -1
            for i in range(len(self.matrix)):
                if self.matrix[i][j] == 1 and i not in banned_rows:
                    curr = i
                    banned_rows.append(i)
                    break
            if curr >= 0:
                for i in range(len(self.matrix)):
                    if i != curr and self.matrix[i][j] == 1:
                        # print "summ", curr, "and", i
                        for sum in range(j, len(self.matrix[0])):
                            self.matrix[i][sum] = (self.matrix[i][sum] + self.matrix[curr][sum]) % 2
            # self.log()
        res = [None] * len(self.matrix[0])
        for i in range(len(self.matrix)):
            ones_in = 0
            indexes = []
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 1:
                    ones_in += 1
                    indexes.append(j)
            if ones_in == 1:
                res[indexes[0]] = 0
            elif ones_in == 2:
                res[indexes[0]] = 1
                res[indexes[1]] = 1
        # delete
        return res
        piv = perm_find(res,0)
        res = []
        # print "solve bf:", piv
        for solve in piv:
            if solve not in ban:
                res.append(copy.copy(solve))
        # print "solve af:", res
        # print "ban:", ban, "\n"
        return res

    def check(self, solve):
        confirmed_solve = []
        add_to_ban = []
        for s in solve:
            flag = True
            for i in range(len(self.matrix)):
                sum = 0
                for j in range(len(s)):
                    sum += s[j] * self.matrix[i][j]
                if sum % 2 != 0:
                    # add s to ban list
                    flag = False
                    break
            if flag:
                confirmed_solve.append(copy.copy(s))
            else:
                add_to_ban.append(copy.copy(s))
        # print add_to_ban
        return confirmed_solve, add_to_ban
