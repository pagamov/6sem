# done
import matplotlib.pyplot as plt
# x**3 + x**2 - x - 0.5
err = 10**-7

def display(x, fx, it):
    print('x =', '{:.8f}'.format(x), 'f(x) =', '{:.8f}'.format(fx), it)

def f(x):
    return x**3 + x**2 - x - 0.5

def diff(f, x):
    dx = 10**-4
    return (f(x + dx) - f(x)) / (dx)

def solve_simple_iter(f, a, b, err):
    step, q, alpha = 0.1, [], diff(f, (a + b) / 2)
    # создание новой функции
    fi = lambda x: x - (1/alpha)*f(x)
    # создание производной новой функции
    diffi = lambda x: (x-(1/alpha)*fi(x + err) - (x-(1/alpha)*fi(x))) / err
    # проверка на сжимающую функицю и нахождение q через максимальную производную
    x = a + err
    while x < b:
        q.append(abs(diffi(x)))
        if fi(x) <= a or fi(x) >= b:
            print("fi(x) not in [a,b] : Error")
            exit()
        elif abs(diffi(x)) > 1:
            print("det fi(x) > 1 : Error")
            exit()
        x += step # check step
    q, x, num_of_it = max(q), (a + b) / 2, 0
    print('q: {:.5f}'.format(q), 'alpha: {:.5f}'.format(1/alpha), 'x_0: {:.5f}'.format(x), sep='; ')
    while True:
        x_ = fi(x)
        num_of_it += 1
        if abs(x - x_) * q / (1 - q) < err:
            display(x_, f(x_), num_of_it)
            return x_, num_of_it
        x = x_

def solve_Newton(f, a, b, err):
    x, num_of_it = (a + b) / 2, 0
    # первая производная
    dif = lambda x: (f(x + err) - f(x)) / err
    # вторая производная
    diff = lambda x: (dif(x + err) - dif(x)) / err

    if f(a) * f(b) >= 0:
        print('f(a)f(b) >= 0 : Error')
        exit()
    if f(x) * diff(x) <= 0:
        print(f(x) * diff(x))
        print("f(x)f''(x) <= 0")
        exit()

    while True:
        x_ = x - f(x) / dif(x)
        num_of_it += 1
        if abs(x - x_) < err:
            display(x_, f(x_), num_of_it)
            return x_, num_of_it
        x = x_

def make_xy(f, a, b):
    x, step = a, 0.1
    x_, y_, xz, yz = [], [], [], []
    while x <= b:
        x_.append(x)
        y_.append(f(x))
        xz.append(x)
        yz.append(0)
        x += step
    return x_, y_, xz, yz

x_, y_, xz, yz = make_xy(f, -2, 2)
plt.plot(x_, y_, label='f(x)')
plt.plot(xz, yz)
plt.legend()
plt.show()

# понимаем что корень больше нуля в пределах 0.5 и 1
print('метод простых итераций')
solve_simple_iter(f, 0.5, 1, err)

print('метод Ньютона')
# если брать а = 0.5 не выполняется второе условие
solve_Newton(f, 0.75, 1, err)
