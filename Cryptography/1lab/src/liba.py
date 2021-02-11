# NOTE 2: find all primes <= B

def prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def find_primes(B):
    res = []
    for i in range(2, B+1):
        if prime(i):
            res.append(i)
    return res

# NOTE 3: find N such N^2 are smooth under B

def smooth_under(number, primes):
    res = []
    for i in range(len(primes)):
        res.append(0)
    i = 0
    while number != 1 and i < len(primes):
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
        # will work later!
        self.ban = []
        for i in range(len(primes)):
            self.matrix.append([])

    def add(self, smooth_number):
        for i in range(len(self.primes)):
            self.matrix[i].append(smooth_number[i])

    def log(self):
        for i in range(len(self.primes)):
            print self.matrix[i]

def make_matrix_smooth(smooth_numbers,primes):
    matrix = []
    for i in range(len(primes)):
        piv = []
        for j in range(len(smooth_numbers)):
            piv.append(smooth_numbers[j][2][i])
        matrix.append(piv)
    return matrix
