


f = lambda x: (3*x + 4) / (2*x + 7)

x_0 = -2
x_1 = 2
h1 = 1
h2 = 0.5

true_integral = 1.777

def rectangle_integration(a, b, h):
    integ,x = 0.0,a
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
