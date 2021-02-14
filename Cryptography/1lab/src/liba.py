import copy
# NOTE 2: find all primes <= B

def eratosthenes(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    return list(filter(lambda x: x != 0, numbers))

# NOTE 3: find N such N^2 are smooth under B

def smooth_under(number, primes):
    res = [0] * len(primes)
    i = 0
    while number > 1 and i < len(primes):
        if number % primes[i] == 0:
            res[i] += 1
            number = number / primes[i]
        else:
            i += 1
    if number != 1:
        return None
    flag = False
    for i in res:
        if i != 0:
            flag = True
    if flag:
        return res
    else:
        return None

# NOTE 4: make matrix from smooth numbers

class Matrix_solver:
    def __init__(self, primes):
        # NOTE: matrix for storage i:primes j:x1,x2,x3,...,xn
        self.matrix = []
        self.primes = primes
        # NOTE: DO NOT TAKE attempts to solve cases we alredy solve!
        self.ban = [[]]
        for i in range(len(primes)):
            self.matrix.append([])

    def add(self, smooth_number):
        for i in range(len(self.primes)):
            self.matrix[i].append(smooth_number[i])
        for i in range(len(self.ban)):
            self.ban[i].append(0)

    def log(self):
        print "matrix:"
        for i in range(len(self.primes)):
            print self.matrix[i]
        print "ban list:"
        for i in range(len(self.ban)):
            print self.ban[i]

    def update_ban(self, ban_list):
        # print "ban list len", len(ban_list)
        for i in range(len(ban_list)):
            self.ban.append(ban_list[i])

def perm_find(arr, pos):
    if None not in arr:
        return [arr]
    if len(arr) == pos:
        # NOTE: end of arr
        return None
    if arr[pos] == None:
        a = copy.copy(arr)
        a[pos] = 0
        b = copy.copy(arr)
        b[pos] = 1
        res1 = perm_find(a, pos+1)
        res2 = perm_find(b, pos+1)
        if res1 != None and res2 != None:
            return res1 + res2
        else:
            return [a,b]
    else:
        return perm_find(arr, pos+1)

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
        print "Gauss_Jordane matrix:"
        for i in range(len(self.matrix)):
            print self.matrix[i]

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

def GCD(m,n):
    mult = 1
    while True:
        if m == 0 or n == 0 or m == n:
            return mult*max(n,m)
        if m == 1 or n == 1:
            return mult*1
        if m % 2 == 0 and n % 2 == 0:
            mult *= 2
            m = m/2
            n = n/2
        if m % 2 == 0 and n % 2 != 0:
            m = m/2
        if m % 2 != 0 and n % 2 == 0:
            n = n/2
        if m % 2 != 0 and n % 2 != 0:
            if n > m:
                piv = (n-m)/2
                n = m
                m = piv
            elif n < m:
                m = (m-n)/2
