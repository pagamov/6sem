import numpy as np
from numpy.linalg import norm, inv

A = [[26,-9,-8,8], [9,-21,-2,8], [-3,2,-18,8], [1,-6,-1,11]]
b = [[20],[-164],[140],[-81]]
err = 10**-4

def transpose(A):
    AT = [[0] for i in range(len(A))]
    for i in range(0, len(A)):
        AT[i][0] = A[i]
    return AT
def sub(A, B):
    C = []
    for i in range(len(A)):
        c_=[]
        for j in range(len(A[0])):
            c_.append(A[i][j] - B[i][j])
        C.append(c_)
    return C
def add(A, B):
    C = []
    for i in range(len(A)):
        c_=[]
        for j in range(len(A[0])):
            c_.append(A[i][j] + B[i][j])
        C.append(c_)
    return C
def mult(A, B):
    C = []
    for i in range(0,len(A)):
        c_ = []
        for j in range(0,len(B[0])):
            elem = 0
            for k in range(0,len(B)):
                elem += A[i][k] * B[k][j]
            c_.append(elem)
        C.append(c_)
    return C

def find_alpha_beta(A, B):
    size = len(A)
    alpha = [[0] * size for i in range(size)]
    beta = [0 for i in range(size)]
    for i in range(size):
        beta[i] = B[i][0] / (A[i][i] ) # + 1e-3
        for j in range(size):
            if i!=j:
                alpha[i][j] = -A[i][j] / (A[i][i] ) #  1e-3
    return alpha, beta
def find_norm(A):
    C = []
    for i in range(0,len(A)):
        suma=0
        for j in range(0,len(A[0])):
            suma += abs(A[i][j])
        C.append(suma)
    return(max(C))
def finish_simple_iter(x, x_prev, norm_alpha, eps):
    norma = find_norm(sub(x,x_prev))
    if norm_alpha == 1:
        return norma <= eps
    else:
        tmp = norm_alpha / (1 - norm_alpha)
        return tmp * norma <= eps
def simple_iter(A, B, eps):
    alpha, beta = find_alpha_beta(A,B)
    beta = transpose(beta)
    x = beta
    k = 0
    while True:
        k += 1
        x_i = add(beta, mult(alpha, x))
        if finish_simple_iter(x_i, x, find_norm(alpha), eps):
            break
        x = x_i
    return x_i , k
def finish_zeidel(x, x_prev, norm_alpha, norm_c, eps):
    norma = norm(x - x_prev)
    if norm_alpha == 1:
        return norma <= eps
    else:
        tmp = norm_c / (1 - norm_alpha)
        return tmp * norma <= eps
def zeidel(A, B, eps):
    alpha, beta = find_alpha_beta(A,B)
    beta = transpose(beta)
    size = len(alpha)

    np_alpha = np.array(alpha)
    np_beta = np.array(beta)
    B = np.tril(np_alpha, -1)
    C = np_alpha - B

    arg1 = inv(np.eye(size, size) - B).dot(C)
    arg2 =  inv(np.eye(size, size) - B).dot(np_beta)

    x = arg2
    k = 0

    while True:
        k += 1
        x_i = arg2 + arg1.dot(x)
        if finish_zeidel(x_i, x, norm(arg1), norm(C), eps):
            break
        x = x_i
    return x_i, k


print('simple iteration:')
print(simple_iter(A,b, err))

print('zeidel:')
print(zeidel(A,b, err))

print('numpy:')
print(np.linalg.solve(A, b))
