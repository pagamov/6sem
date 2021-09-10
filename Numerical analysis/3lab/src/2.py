# done
from math import pi, tan, sin, pow, sqrt
import numpy as np
import matplotlib.pyplot as plt
import copy

# cubic spline

x_star = 2.666667

x = [1,1.9,2.8,3.7,4.6]
y = [2.4142,1.0818,0.50953,0.11836,-0.24008]

# x = [0,1,2,3,4]
# y = [0,1,-1,2,-2]

# x = [0,1.7,3.4,5.1,6.8,8.5]
# y = [0.4713,1.0114,1.5515,2.0916,2.6317,3.1718]

def make_spline_matrix(x, y, n, err=10**-10, text=False, X=None):
    # сделаем матрицу коэф а размерности n+1
    A, b, n = [], [], n+1
    for i in range(n):
        r = []
        for j in range(n):
            if i == 0 and j == 0:
                r.append(len(x))
            else:
                r.append(sum(map(lambda a: pow(a,i+j),x)))
        A.append(r)
        b.append(sum(map(lambda a,b: pow(a,i) * b,x,y)))
    if text:
        print('Matrix A and b')
        for i in range(len(A)):
            for j in range(len(A[i])):
                print('{:.2f}'.format(A[i][j]), end='  ')
            print('['+'{:.2f}'.format(b[i])+']')
    # Теперь имея матрицу и правую часть решим ее зейделем с точностью err
    a_,a = [None] * len(A),[0] * len(A)
    while True:
        for i in range(len(A)):
            s = 0
            for j in range(len(A)):
                if j < i:
                    s += A[i][j] * a_[j]
                elif i != j:
                    s += A[i][j] * a[j]
            a_[i] = (b[i] - s) / A[i][i]
        if sqrt(sum(map(lambda a,b: pow(a - b,2),a,a_))) < err:
            break
        a = copy.copy(a_)
    if text:
        print('f(x) = ', float('{:.4f}'.format(a_[0])), end='')
        for i in range(1, len(a_)):
            print(' +', str(float('{:.4f}'.format(a_[i]))) + '*x^' + str(i),end='')
        print()
    # теперь сделаем итоговые координаты
    resx,resy = [],[]
    start = x[0]
    while start < x[-1]:
        resx.append(start)
        resy.append(sum([a_[j] * pow(start, j) for j in range(len(a_))]))
        start += 0.1 # сделать другой step
    # вычислим квадрат ошибок
    if text:
        yy = [sum([a_[j] * pow(num, j) for j in range(len(a_))]) for num in x]
        print('error =', sqrt(sum(list(map(lambda a, b: pow(a - b,2), yy, y)))))
    # возвратим результат
    if X != None:
        return sum([a_[j] * pow(X, j) for j in range(len(a_))])
    else:
        return resx, resy

x_, y_ = make_spline_matrix(x, y, 3, err=10**-2, text=True)

print('Y =', make_spline_matrix(x, y, 3, err=10**-2, text=False, X = x_star))

plt.plot(x, y, label='main')
plt.plot(x_, y_, label='spline')
plt.legend()
plt.show()
