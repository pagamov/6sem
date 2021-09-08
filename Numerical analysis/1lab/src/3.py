# done
import copy
import numpy as np
import math

A = [[26,-9,-8,8], [9,-21,-2,8], [-3,2,-18,8], [1,-6,-1,11]]
b = [20,-164,140,-81]
err = 10**-4

def display(m,t):
    print(t)
    for row in m:
        print(row)
    print('')

def sufficient_condition(A, b):
    # if //alpha// < 1 then ok
    alpha = copy.deepcopy(A)
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i == j:
                alpha[i][j] = 0
            else:
                alpha[i][j] = -A[i][j] / A[i][i]
    return abs(np.linalg.det(alpha))

def error(x,x_, err):
    if x_[0] == None:
        return False
    res = [0] * len(x)
    for i in range(len(x)):
        res[i] = pow(x[i] - x_[i],2)
    if math.sqrt(sum(res)) > err:
        return False
    else:
        return True

def solve(A, b, err):
    x_ = [None] * len(A)
    x = [0] * len(A)
    num_of_it = 0
    while True:
        for i in range(len(A)):
            s = 0
            for j in range(len(A)):
                if i != j:
                    s += A[i][j] * x[j]
            x_[i] = (b[i] - s) / A[i][i]
        num_of_it += 1
        if error(x,x_,err):
            break
        x = copy.copy(x_)
    return x_, num_of_it


def solveZeidel(A, b, err):
    x_ = [None] * len(A)
    x = [0] * len(A)
    num_of_it = 0
    while True:
        for i in range(len(A)):
            s = 0
            for j in range(len(A)):
                if j < i:
                    s += A[i][j] * x_[j]
                elif i != j:
                    s += A[i][j] * x[j]
            x_[i] = (b[i] - s) / A[i][i]
        num_of_it += 1
        if error(x,x_,err):
            break
        x = copy.copy(x_)
    return x_, num_of_it

def prove(A, x, b):
    n = len(A)
    res = [0] * n
    for i in range(n):
        for j in range(n):
            res[i] += A[i][j] * x[j]
        res[i] -= b[i]
    return res

display(A,'matrix A')
display([b],'b vector')
display([sufficient_condition(A,b)], 'sufficient_condition < 1')

print('ordinary method')
x, it = solve(A, b, err)
display([x], 'x vector')
display([it], 'num_of_iterations')
display([prove(A, x, b)], 'prove for x')

print('Zeidel method')
x, it = solveZeidel(A, b, err)
display([x], 'x vector')
display([it], 'num_of_iterations')
display([prove(A, x, b)], 'prove for x')
