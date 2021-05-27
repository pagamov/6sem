from math import pi, tan, sin
import numpy as np
import matplotlib.pyplot as plt

# cubic spline

x_star = 2.666667

# x = [1,1.9,2.8,3.7,4.6]
# y = [2.4142,1.0818,0.50953,0.11836,-0.24008]

x = [0,1,2,3,4]
y = [0,1.8415,2.9093,3.1411,3.2432]

def display(m,b):
    for i in range(len(m)):
        print(m[i], end=' ')
        print('['+str(b[i])+']')

def make_b_spline_matrix(x,y):
    matrix = []
    b = [0] * len(x)
    for i in range(len(x)):
        matrix.append([0]*len(x))
    for i in range(len(x)):
        if i == 0:
            matrix[i][1] = 2 * ((x[1] - x[0]) + (x[2] - x[1]))
            matrix[i][2] = (x[2] - x[1])
            b[0] = 3 * ((y[2]-y[1])/(x[2]-x[1]) - ((y[1]-y[0])/(x[1]-x[0])))
        elif i == len(x) - 1:
            pass
        else:
            pass


    display(matrix,b)

make_b_spline_matrix(x, y)
