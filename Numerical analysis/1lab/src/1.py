import copy

def m_zero(n):
    res = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append(0)
        res.append(r)
    return res

class LU:
    def __init__(self, A, n):
        self.U = copy.deepcopy(A)
        self.L = m_zero(n)

        for i in range(n):
            for j in range(i,n):
                self.L[j][i] = self.U[j][i] / self.U[i][i]

        for k in range(1, n):
            for i in range(k-1,n):
                for j in range(i,n):
                    self.L[j][i] = self.U[j][i] / self.U[i][i];
            for i in range(k,n):
                for j in range(k-1,n):
                    self.U[i][j] = self.U[i][j] - self.L[i][k-1] * self.U[k-1][j];
    def show(self):
        print "U matrix"

        for i in range(len(self.U)):
            print self.U[i]

        print "\nL matrix"

        for i in range(len(self.L)):
            print self.L[i]
    def prois(self):
        n = len(self.U)
        R = m_zero(n)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    R[i][j] += self.L[i][k] * self.U[k][j]
        return R


if __name__ == '__main__':
    A = [[-1,-7,-3,-2],
         [-8,1,-9,0],
         [8,2,-5,-3],
         [-5,3,5,-9]]
    b = [-12,-60,-91,-43]

    for i in range(len(A)):
        print A[i]
    print '\n', b

    lu = LU(A,len(A))
    lu.show()

    R = lu.prois()
    print "R"
    for i in range(len(R)):
        print R[i]

