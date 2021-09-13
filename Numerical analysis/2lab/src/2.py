# done
from math import cos, sin, log10

def f1(x,y):
    return x - cos(y) - 1
def f2(x,y):
    return y - log10(x+1) - 1
def fi1(x,y):
    return cos(y) + 1
def fi2(x,y):
    return log10(x+1) + 1

def solve_simple_iter(fi1, fi2, x, y, err):
    num_of_it = 0
    while True:
        x_, y_ = fi1(x,y), fi2(x,y)
        num_of_it += 1
        if max(abs(x - x_), abs(y - y_)) < err:
            print('x = {:.8f}; y = {:.8f}; f1 = {:.6f}; f2 = {:.6f};'.format(x,y,f1(x,y),f2(x,y)), num_of_it)
            break
        x, y = x_, y_

def solve_Newton(f1, f2, x, y, err):
    num_of_it = 0
    dif1 = lambda f,x,y: (f(x + err,y) - f(x,y)) / err #производная по x
    dif2 = lambda f,x,y: (f(x,y + err) - f(x,y)) / err #производная по y
    det = lambda A: A[0][0]*A[1][1] - A[0][1]*A[1][0]  #детерминант матрицы
    while True:
        A1 = det([[f1(x,y),dif2(f1,x,y)],
                  [f2(x,y),dif2(f2,x,y)]])
        A2 = det([[dif1(f1,x,y),f2(x,y)],
                  [dif1(f2,x,y),f2(x,y)]])
        J  = det([[dif1(f1,x,y),dif2(f1,x,y)],
                  [dif1(f2,x,y),dif2(f2,x,y)]])
        x_, y_ = x - A1 / J, y - A2 / J
        num_of_it += 1
        if max(abs(x - x_), abs(y - y_)) < err:
            print('x = {:.8f}; y = {:.8f}; f1 = {:.6f}; f2 = {:.6f};'.format(x,y,f1(x,y),f2(x,y)), num_of_it)
            break
        x, y = x_, y_

x_s,y_s = 0.5,0.5
err = 10**-4

print('метод простых итераций')
solve_simple_iter(fi1, fi2, x_s, y_s, err)

print('метод Ньтона')
solve_Newton(f1, f2, x_s, y_s, err)
