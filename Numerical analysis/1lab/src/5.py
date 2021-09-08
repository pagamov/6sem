# done
import math, copy, numpy as np

A = [[3,-7,-1, 1],
    [-9,-8, 7, 6],
    [ 5, 2, 2, 9],
    [ 6, 7 ,4 ,3]]

# A = [[1,3,1],[1,1,4],[4,3,1]]
A = [[-4,-6,-3],[-1,5,-5],[6,2,5]]
err = 10**-4

# λ_1≈7,112
# λ_2≈-0,556-3,821*i
# λ_3≈-0,556+3,821*i

def display(m, t):
    print(t)
    n = 5
    template = '{:.' + str(n) + 'f}'
    for row in m:
        for num in row:
            print(str(template.format(num)), end='  ')
        print()
    print('')

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

def find_housholder(A, it):
    v = [0] * len(A)
    for i in range(it, len(A)):
        v[i] = A[i][it]
    s = 0
    for i in range(len(A)):
        s += math.pow(v[i],2)
    if A[it][it] < 0:
        v[it] -= math.sqrt(s)
    elif A[it][it] > 0:
        v[it] += math.sqrt(s)
    else:
        print('eq 0 house')
    H = copy.deepcopy(A)
    dim = 0
    for i in range(len(v)):
        dim += math.pow(v[i],2)
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                H[i][j] = 1 - 2 * v[i] * v[j] / dim
            else:
                H[i][j] = 0 - 2 * v[i] * v[j] / dim
    return H

def find_QR(A):
    R_ = copy.deepcopy(A)
    Q_ = None
    for i in range(len(R_) - 1):
        H = find_housholder(R_, i)
        if Q_ == None:
            Q_ = H
        else:
            Q_ = prois(H, Q_)
        R_ = prois(R_, H)
    return Q_, R_

def error(A, A_, err):
    s = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if j == 0 and i > j:
                s += math.pow(A_[i][j], 2)
    if math.sqrt(s) < err:
        return True
    return False

def solve_QR(A):
    iter = 0
    Q,R = find_QR(A)
    A_ = prois(Q, R)
    while error(A, A_, err) != True:
        Q,R = find_QR(A)
        A = A_
        A_ = prois(Q, R)
        iter += 1
    print('iter:',iter)
    return A_

def solve_roots(A):
    res = [A[0][0]]
    x = A[1][1]
    y = A[2][2]
    z = A[1][2] * A[2][1]
    D = (x+y)*(x+y)-4*(x*y-z)
    res.append([(x+y)/2, math.sqrt(-D)/2])
    res.append([(x+y)/2, -math.sqrt(-D)/2])
    return res

A_ = solve_QR(A)
display(A_, 'A_')
print(solve_roots(A_))
