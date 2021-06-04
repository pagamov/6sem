from math import exp, sin, cos
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

l = 0.1
a = 0.1
alpha = 0.2
time = 0

def fi(n):
    return (8.4 + 10*n*3.14)

def ksi(n):
    return ((alpha + fi(n)) / (fi(n) - alpha * 3.14 / 2))

def f(x,t):
    n = 0
    res = 1000
    while n < 10:
        up = (-300+1000) * (sin(fi(n)*x) - ksi(n)*cos(fi(n)*l) + ksi(n)) / fi(n)
        down = -2*fi(n)*(ksi(n)**2+1) + (ksi(n)**2-1)*sin(2*fi(n)*l) + 2*ksi(n)*cos(2*fi(n)*l)
        right = (cos(fi(n)*x) + ksi(n)*sin(fi(n)*x))
        rr = exp(-1*(a**2)*fi(n)*t)
        res += up * right * rr / down
        n += 1
    return res

def get_data(start,end,t):
    x = []
    y = []
    while start < end:
        x.append(start)
        y.append(f(start,t))
        start += 0.005
    return x,y

while time < 50:
    x, y = get_data(0,l,time)
    plt.plot(x, y, label='t = ' + str(time))
    time += 10

plt.xlabel('X')
plt.ylabel('T')
plt.title('1 task')
plt.legend()
plt.show()
