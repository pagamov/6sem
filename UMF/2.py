from math import exp, sin, cos
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

l = 0.1
# a = 10**(-3)
alpha = 10**(-3)
pi = 3.14
time = 0


def fi(n):
    return (0 + 10*n*3.14)

def f(x,t):
    n = 2
    res = exp(-t) * (1 - alpha * x) / (1 - alpha * l)
    while n < 10:
        up1 = -1*alpha*(sin(fi(n)*l) - fi(n)*l) + (fi(n) * cos(fi(n)*l) - fi(n))
        down1 = (l/2 - alpha / (fi(n)**2 + alpha**2)) * (1 - alpha * l) * fi(n) * fi(n)
        r11 = cos(alpha * fi(n) * t) - sin(alpha*fi(n)*t) / (fi(n)*alpha)
        r21 = sin(fi(n)*(x - l))


        up2 = fi(n) * cos(fi(n) * l) - alpha*(sin(fi(n)*l) - fi(n)*l)

        down2 = (l/2 - alpha / (fi(n)**2 + alpha**2)) * (1 - alpha * l) * fi(n)**2 * (alpha**3 * fi(n)**3 + alpha*fi(n))
        r21 = (alpha * fi(n) - alpha * fi(n) * exp(-t) * cos(alpha*fi(n)*t) - exp(-t) * sin(alpha* fi(n) * t)) * cos(alpha * fi(n) * t) - (1 - exp(-t)*cos(alpha * fi(n) * t) + alpha* fi(n)*sin(alpha * fi(n) * t)) * sin(alpha * fi(n) * t)
        r22 = sin(fi(n)*(x - l))

        res += up1 * r11 * r21 / down1
        res += up2 * r21 * r22 / down2

        n += 1
    return res


def get_data(start,end,t):
    x = []
    y = []
    while start < end:
        x.append(start)
        y.append(f(start,t)-1)
        start += 0.0001
    return x,y

# while time < 10:
x, y = get_data(0,l,time)
plt.plot(x, [0]*len(x), label='t = ' + str(time))


time += 0.005

plt.xlabel('X')
plt.ylabel('Y')
plt.title('2 task')
plt.legend()
plt.show()

x, y = get_data(0,l,time)
plt.plot(x, y[::-1], label='t = ' + str(time))
time += 0.005

plt.xlabel('X')
plt.ylabel('Y')
plt.title('2 task')
plt.legend()
plt.show()

x, y = get_data(0,l,time)
plt.plot(x, y[::-1], label='t = ' + str(time))

plt.xlabel('X')
plt.ylabel('Y')
plt.title('2 task')
plt.legend()
plt.show()
