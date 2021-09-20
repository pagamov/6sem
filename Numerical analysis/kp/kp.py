# Сингулярное разложение матрицы
# Матрица А
# Сначала ищем А^T * A
# получаем собств значения
# находим их собств векторы
# нормируем векторы - это строчки правой матрциы разложения
# ищем А * A^T
# получаем собств значения
# находим их собств векторы
# нормируем векторы - это стоблцы левой матрциы разложения
# составляем матрицы 3 штуки
# глав диагональ средней - корни собств значений - сингулярные корни

import copy
import math

def display(m, t=''):
    if t != '':
        print(t)
    for row in m:
        print(row)

def find_max(A):
    m, ib, jb = None, None, None
    for i in range(len(A)):
        for j in range(i,len(A)):
            if i < j:
                if m == None or abs(A[i][j]) > m:
                    m = abs(A[i][j])
                    ib, jb = i, j
    return ib, jb

def error(A_):
    s = 0
    for i in range(len(A_)):
        for j in range(i+1, len(A_)):
            if i < j:
                s += math.pow(A_[i][j], 2)
    return s**0.5

def transpose(A):
    return [[row[i] for row in A] for i in range(len(A[0]))]

def rotate_matrix(A,s,c,i,j):
    res = [[0 for l in range(A)] for k in range(A)]
    for k in range(A):
        res[k][k] = 1
    res[i][i] = c
    res[i][j] = -s
    res[j][i] = s
    res[j][j] = c
    return res

def prois(U, L, D=None):
    if (len(U[0]) == len(L)):
        R = [[sum([U[i][k] * L[k][j] for k in range(len(U[i]))]) for j in range(len(L[0]))] for i in range(len(U))]
        if D != None:
            return prois(R,D)
        return R
    else:
        print('err in Mult')
        exit()

def jacobi(A):
    err = 0.1
    U = None
    while True:
        i, j = find_max(A)
        P = math.pi / 4
        if A[i][i] - A[j][j] != 0:
            P = 2 * A[i][j] / (A[i][i] - A[j][j])
        c = math.cos(math.atan(P) / 2)
        s = math.sin(math.atan(P) / 2)
        rotate = rotate_matrix(len(A),s,c,i,j)
        if U == None:
            U = copy.deepcopy(rotate)
        else:
            U = prois(U, rotate)
        A = prois(prois(transpose(rotate),A),rotate)
        er = error(A)
        if er < err:
            break
    res = []
    for i in range(len(A)):
        vec = [U[j][i] for j in range(len(A))]
        vecs = sum([x**2 for x in vec])**0.5
        if vecs != 0:
            vec = [x / vecs for x in vec]
        res.append([A[i][i],vec])
    return res

# A = [[1,0,0,0,2],
#      [0,0,3,0,0],
#      [0,0,0,0,0],
#      [0,4,0,0,0]]
A = [[2,6],[5,3],[-4,0]]
# A = [[2,6,5,2],[5,3,0,1],[-4,0,-5,10]]
# A = [[4,2,1],[2,5,3],[1,3,6]]

def SVD(A, cut=0):
    A1res = sorted(jacobi(prois(transpose(A),A)))[::-1]
    A2res = sorted(jacobi(prois(A,transpose(A))))[::-1]
    right = [[A1res[i][1][j] for j in range(len(A1res))] for i in range(len(A1res))]
    left = [[A2res[j][1][i] for j in range(len(A2res))] for i in range(len(A2res))]
    center = copy.deepcopy(A)
    center = [[0 for j in range(len(A[i]))] for i in range(len(A))]
    for i in range(min(len(A),len(A[0]))):
        center[i][i] = A1res[i][0]**0.5
    if cut != 0 and cut < 100:
        f_vert = max(math.floor(len(center) * (100 - cut) / 100),1)
        f_hor = max(math.floor(len(center[0]) * (100 - cut) / 100),1)
        left = [[left[i][j] for j in range(f_vert)] for i in range(len(left))]
        right = [[right[i][j] for j in range(len(right[0]))] for i in range(f_hor)]
        center = [[center[i][j] for j in range(f_hor)] for i in range(f_vert)]
        return left, center, right
    else:
        return left, center, right

import matplotlib.pyplot as plt
import random

x = [i for i in range(1,25)]
A = [
[(random.randint(-5,5)) for i in x],
[(random.randint(-10,10)) for i in x],
[(random.randint(-7,7)) for i in x],
]

fig, axs = plt.subplots(4)
axs[0].plot(x, A[0],'r', label = 'data 1')
axs[0].plot(x, A[1],'g', label = 'data 2')
axs[0].plot(x, A[2],'y', label = 'data 2')
axs[0].grid()
axs[0].legend()

L,C,R = SVD(A,20)
A_ = prois(L,C,R)

axs[1].plot(x, A_[0],'r', label = 'data 20%')
axs[1].plot(x, A_[1],'g', label = 'data 20%')
axs[1].plot(x, A_[2],'y', label = 'data 20%')
axs[1].grid()
axs[1].legend()

L,C,R = SVD(A,50)
A_ = prois(L,C,R)

axs[2].plot(x, A_[0],'r', label = 'data 50%')
axs[2].plot(x, A_[1],'g', label = 'data 50%')
axs[2].plot(x, A_[2],'y', label = 'data 50%')
axs[2].grid()
axs[2].legend()

L,C,R = SVD(A,90)
A_ = prois(L,C,R)

axs[3].plot(x, A_[0],'r', label = 'data 90%')
axs[3].plot(x, A_[1],'g', label = 'data 90%')
axs[3].plot(x, A_[2],'y', label = 'data 90%')
axs[3].grid()
axs[3].legend()

plt.show()
