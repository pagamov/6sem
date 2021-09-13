# done
import copy
import math
# https://old.math.tsu.ru/EEResources/cm/text/6_2_3.htm
A = [[8,2,-1], [2,-5,-8], [-1,-8,-5]]
err = 10**-2

# λ_1≈-13.024
# λ_2≈2.225
# λ_3≈8.799

def display(m, t):
    print(t)
    for row in m:
        print(row)
    print('')

def find_max(A):
    m, ib, jb = None, None, None
    for i in range(len(A)):
        for j in range(len(A)):
            if i < j:
                if m == None or abs(A[i][j]) > m:
                    m = A[i][j]
                    ib, jb = i, j
    return ib, jb

def error(A_, err):
    res,s = [0] * len(A_),0
    for i in range(len(A_)):
        for j in range(len(A_)):
            if i < j:
                s += math.pow(A_[i][j], 2)
    if math.sqrt(s) > err:
        return False
    else:
        return True

def transpose(A):
    res = copy.deepcopy(A)
    for i in range(len(A)):
        for j in range(len(A)):
            res[i][j] = A[j][i]
    return res

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
        c = math.cos(math.atan(P) / 2)
        s = math.sin(math.atan(P) / 2)
        rotate = rotate_matrix(A,s,c,i,j)
        A_ = prois(transpose(rotate),prois(A,rotate))
        num_of_it += 1
        A = copy.deepcopy(A_)
        if error(A_, err):
            break
    return A, num_of_it

def get_self_number(A):
    res = []
    for i in range(len(A)):
        res.append(A[i][i])
    return sorted(res)

display(A, "A matrix")
matrix, it = jacobi(A, err)
display(matrix,'after jacobi')
display([it],'iteration')
display([get_self_number(matrix)],'res')
