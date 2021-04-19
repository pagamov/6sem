import copy
import math
# https://old.math.tsu.ru/EEResources/cm/text/6_2_3.htm
A = [[8,2,-1], [2,-5,-8], [-1,-8,-5]]
err = 10**-4

def display(A, word):
    print('\n' + word)
    for line in A:
        print(line)
display(A, "A matrix")
def find_max(A):
    m = -10**100
    ib,jb = None, None
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j and abs(A[i][j]) > m:
                m = A[i][j]
                ib, jb = i, j
    if ib < jb:
        return ib, jb
    else:
        return jb, ib
def error(A, A_, err):
    res = [0] * len(A)
    for i in range(len(A)):
        res[i] = abs(A[i][i] - A_[i][i])
    if max(res) > err:
        return False
    else:
        return True
def rotate_matrix(A,s,c,i,j):
    res = copy.deepcopy(A)
    for k in range(len(A)):
        for l in range(len(A)):
            if k == l:
                res[k][l] = 1
            else:
                res[k][l] = 0
    res[i][i] = c
    res[i][j] = -s
    res[j][i] = s
    res[j][j] = c
    return res
def m_zero(n):
    res = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append(0)
        res.append(r)
    return res
def prois(U, L):
    n = len(U)
    R = m_zero(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                R[i][j] += L[i][k] * U[k][j]
    return R
def jacobi(A, err):
    A_ = copy.deepcopy(A)
    num_of_it = 0

    while True:
        i, j = find_max(A)
        P = math.pi / 4
        if A[i][i] - A[j][j] != 0:
            P = 2 * A[i][j] / (A[i][i] - A[j][j])
        c = math.cos(math.atan(P)/2)
        s = math.sin(math.atan(P)/2)

        # rotate = rotate_matrix(A,s,c,i,j)
        # # display(rotate,'rotate')
        # A_ = prois(rotate, A)
        A_ = prois(rotate_matrix(A,s,c,i,j), A)
        if abs(A_[i][j]) > abs(A[i][j]):
            print(A_[i][j], A[i][j])
            exit()
        # for k in range(len(A)):
        #     for l in range(len(A)):
        #         if k not in [i,j] and l not in [i,j]:
        #             A_[k][l] = A[k][l]
        #         elif k == i and l not in [i,j]:
        #             A_[i][l] = A[i][l] * c + A[j][l] * s
        #         elif k == j and l not in [i,j]:
        #             A_[j][l] = -1 * A[i][l] * s + A[j][l] * c
        #         elif k not in [i,j] and l == i:
        #             A_[k][i] = A[k][i] * c + A[k][j] * s
        #         elif k not in [i,j] and l == j:
        #             A_[k][j] = -1 * A[k][i] * s + A[k][j] * c
        #         elif k == i and l == i:
        #             A_[i][i] = (A[i][i]*c+A[j][i]*s)*c+(A[i][j]*c+A[j][j]*s)*s
        #         elif k == j and l == i:
        #             A_[j][i] = (-1*A[i][i]*s+A[j][i]*c)*c+(-1*A[i][j]*s+A[j][j]*c)*s
        #         elif k == j and l == j:
        #             A_[j][i] = -1*(-1*A[i][i]*s+A[j][i]*c)*s+(-1*A[i][j]*s+A[j][j]*c)*c
        #         elif k == i and l == j:
        #             A_[j][i] = -1*(A[i][i]*c+A[j][i]*s)*s+(A[i][j]*c+A[j][j]*s)*c
        #         else:
        #             print('LOL')
        #             exit()
        # if error(A, A_, err):
        #     # print('exit')
        #     break
        A = copy.deepcopy(A_)
        num_of_it += 1
        if num_of_it == 100:
            break

        # display(A,'iteration ' + str(num_of_it))
    return A, num_of_it
matrix, it = jacobi(A, err)
display(matrix,'after jacobi')
display([it],'iteration')
