import copy
import math
# https://old.math.tsu.ru/EEResources/cm/text/6_2_3.htm
A = [[8,2,-1], [2,-5,-8], [-1,-8,-5]]
err = 10**-4

# λ_1≈-13.024
# λ_2≈2.225
# λ_3≈8.799

def display(m,t):
    """
    display matrix row by row and print text t before it
    """
    print(t)
    for row in m:
        print(row)
    print('')
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
        c = math.cos(math.atan(P)/2)
        s = math.sin(math.atan(P)/2)
        rotate = rotate_matrix(A,s,c,i,j)
        A_ = prois(transpose(rotate),prois(A,rotate))
        num_of_it += 1
        if error(A, A_, err):
            break
        A = copy.deepcopy(A_)
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
