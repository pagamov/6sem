from math import exp, sin, cos
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

l = 0.1
a = 10**(-3)
b = 5.7 * 10**(-5) * 2
N = 1000
time = 10
pi = 3.14

def v(x,t):
    return w1(x,t) + w2(x,t)

def w1(x,t):
    return z1(x,t) + z2(x,t)

def w2(x,t):
    return -100 * exp(b*t) * x / l + 500 * exp(b*t)

def z1(x,t):
    n = 1
    res = 0
    while n < N:
        up = 200*((-1)**n - 2)
        up *= exp((a)**2 * pi*n/l * t)
        up *= sin(pi*n*x/l)
        up /= (pi*n/l) * l
        res += up
        n += 1
    return res

def z2(x,t):
    n = 1
    res = 0
    while n < N:
        up = -150 - 600 * (-1)**n * 2 * b
        up *= exp(-(pi*n*a/l)**2 * t) - (1+b)
        up *= sin(pi*n*x/l)
        up /= (pi*n/l) * l * ((pi*n*a/l)**2 + b)
        res += up
        n += 1
    return res

def u(x,t):
    return v(x,t) * exp(-1*b*t)

def get_data(start,end,t):
    x = []
    y = []
    while start <= end:
        x.append(start)
        y.append(u(start,t))
        start += 0.001
    return x,y

# while time <= 0:
x, y = get_data(0,l,time)
plt.plot(x, y, label='t = ' + str(time))
# time += 5

plt.xlabel('X')
plt.ylabel('T')
plt.title('1 task')
plt.legend()
plt.show()
