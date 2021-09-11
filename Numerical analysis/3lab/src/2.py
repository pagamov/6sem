from math import pi, tan, sin, pow, sqrt
import numpy as np
import matplotlib.pyplot as plt
import copy

x = [1,1.9,2.8,3.7,4.6]
y = [2.4142,1.0818,0.50953,0.11836,-0.24008]

x_star = 2.66666667

x = [0,1,2,3,4]
y = [0,1.8415,2.9093,3.1411,3.2432]

def display(A):
    for row in A:
        for i in range(len(row)):
            print(row[i], end=' ')
        print()

def display(A,b):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print('{:.2f}'.format(A[i][j]), end=' ')
        print('[{:.2f}]'.format(b[i]))

def cubic_spline(x,y):
    # матрица x, y и коэф a,b,c,d
    A = []
    for i in range(1, len(x)):
        A.append([[x[i-1],x[i]],[y[i-1],y[i]],0,0,0,0])
    # display(A)
    # составим матрицу относительно c
    n = len(x)
    h = lambda it: x[it] - x[it-1]
    f = lambda it: y[it]
    M = []
    b = []
    for i in range(1,n+1):
        r = [0] * (n)
        M.append(r)
        b.append(0)
    for i in range(2,n+1):
        if i == 2:
            M[i][2] = 2 * (h(1) + h(2))
            M[i][3] = h(2)
            b[i] = 3 * ((f(2) - f(1)) / h(2) - (f(1) - f(0)) / h(1))
        elif i == n:
            M[n-1][n-2] = h(n-3)
            M[n-1][n-1] = 2 * (h(n-2) + h(n-1))
            b[n-1] = 3 * ((f(n-1) - f(n-2)) / h(n-1) - (f(n-2) - f(n-3)) / h(n-2))
        # else:
        #     M[i][i] = h(i-2)
        #     M[i][i+1] = 2 * (h(i+1) + h(i))
        #     M[i][i+2] = 5
        #     b[i] = 3 * ((f(n-1) - f(n-2)) / h(n-1) - (f(n-2) - f(n-3)) / h(n-2))
    display(M,b)




cubic_spline(x,y)

# plt.plot(x, y, label='main')
# plt.plot(x_1, y_1, label='spline 1')
# plt.legend()
# plt.show()
