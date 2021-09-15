import numpy as np
import matplotlib.pyplot as plt


f = lambda x: (3*x+4) / (2*x+7)
x_0 = -2.0
x_1 = 2.0
h1 = 1.0
h2 = 0.5

accuracy = lambda f1,f2: abs(f1 - f2)

I = 1.77777

def rectangle_integration(a, b, h):
    integ = 0.0
    x = a
    while x < b:
        integ += f(x + h / 2)
        x += h
    return h*integ

def trapeze_integration(a, b, h):
    integ = f(a) / 2
    x = a + h
    while x < b:
        integ += f(x)
        x += h
    return h*(integ + f(x) / 2)

def simpson_integration(a, b, h):
    integ = 0.0
    x = a + h
    while x < b:
        integ += f(x - h) + 4*f(x) + f(x + h)
        x += h + h
    return h*integ/3

def runge_romberg_richardson(h1, F1, h2, F2, p):
    if h1 < h2:
        return F1 + (F1 - F2) / ((h2 / h1)**p - 1)
    else:
        return F2 + (F2 - F1) / ((h1 / h2)**p - 1)

R1 = rectangle_integration(x_0, x_1, h1)
R2 = rectangle_integration(x_0, x_1, h2)

T1 = trapeze_integration(x_0, x_1, h1)
T2 = trapeze_integration(x_0, x_1, h2)

S1 = simpson_integration(x_0, x_1, h1)
S2 = simpson_integration(x_0, x_1, h2)

RRR_R = runge_romberg_richardson(h1, R1, h2, R2, 2)
RRR_T = runge_romberg_richardson(h1, T1, h2, T2, 2)
RRR_S = runge_romberg_richardson(h1, S1, h2, S2, 4)

accuracy(RRR_R, I)
accuracy(RRR_T, I)
accuracy(RRR_S, I)

print('rectangle_integration',R1,h1,R2,h2)
print('trapeze_integration',T1,h1,T2,h2)
print('simpson_integration',S1,h1,S2,h2)


x = [0.01,0.02,0.025,0.05, 0.1, 0.2, 0.25, 0.5]

y1 = list(map(lambda step: accuracy(RRR_R, rectangle_integration(x_0, x_1, step)), x))
y2 = list(map(lambda step: accuracy(RRR_T, trapeze_integration(x_0, x_1, step)), x))
y3 = list(map(lambda step: accuracy(RRR_S, simpson_integration(x_0, x_1, step)), x))

# fig = plt.figure(figsize=(10, 5))

plt.plot(x, y1,'r', label = 'Rectangle integration')
plt.plot(x, y2,'g', label = 'Trapeze integration')
plt.plot(x, y3,'b', label = 'Simpson integration')

plt.xlabel('h')
plt.ylabel('accuracy')

plt.title('Dependence the accuracy from step')

plt.legend(loc='upper center')
# plt.legend()
# plt.show()


x = [(x_1 - x_0) / i + 0.000001 for i in range(6, 14, 2)]

y1 = list(map(lambda step: np.log(accuracy(RRR_R, rectangle_integration(x_0, x_1, step))), x))
y2 = list(map(lambda step: np.log(accuracy(RRR_T, trapeze_integration(x_0, x_1, step))), x))
y3 = list(map(lambda step: np.log(accuracy(RRR_S, simpson_integration(x_0, x_1, step))), x))

# fig = plt.figure(figsize=(10, 5))

plt.plot(x, y1,'r', label = 'Rectangle integration')
plt.plot(x, y2,'g', label = 'Trapeze integration')
plt.plot(x, y3,'b', label = 'Simpson integration')

plt.xlabel('h')
plt.ylabel('log_accuracy')

plt.title('Dependence the accuracy from step')
plt.legend(loc='upper center')

# plt.legend()
# plt.show()
