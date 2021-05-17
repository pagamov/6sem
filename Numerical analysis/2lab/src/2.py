from math import cos, sin, log10

# make err from vector norm

def f1(x,y):
    return x - cos(y) - 1
def f2(x,y):
    return y - log10(x+1) - 1

def fi1(x,y):
    return cos(y) + 1
def fi2(x,y):
    return log10(x+1) + 1

err = 10**-4
x_s,y_s = 0.5,0.5

print('метод простых итераций')
x, y = x_s, y_s
num_of_it = 0
while True:
    x_, y_ = fi1(x,y), fi2(x,y)
    num_of_it += 1
    if abs(x - x_) < err and abs(y - y_) < err:
        print(x, y, f1(x,y), f2(x,y), num_of_it)
        break
    x, y = x_, y_

def J(x,y):
    a11 = 1
    a12 = sin(y)
    a21 = -1/((x+1)*10)
    a22 = 1
    return a11*a22 - a12*a21
def A1(x,y):
    a11 = f1(x,y)
    a12 = sin(y)
    a21 = f2(x,y)
    a22 = 1
    return a11*a22 - a12*a21
def A2(x,y):
    a11 = 1
    a12 = f1(x,y)
    a21 = -1/((x+1)*10)
    a22 = f2(x,y)
    return a11*a22 - a12*a21

print('метод Ньтона') # call it other way???
x, y = x_s, y_s
num_of_it = 0
while True:
    x_, y_ = x - A1(x,y) / J(x,y), y - A2(x,y) / J(x,y)
    num_of_it += 1
    if abs(x - x_) < err and abs(y - y_) < err:
        print(x, y, f1(x,y), f2(x,y), num_of_it)
        break
    x, y = x_, y_
