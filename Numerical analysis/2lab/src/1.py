# x**3 + x**2 - x - 0.5

# new err function based on book
# add checks 

def f(x):
    return x**3 + x**2 - x - 0.5

def fp(x):
    return 3*(x**2) + 2*x - 1

x_s = 0.5
err = 10**-4

print('метод простых итераций')
x = x_s
num_of_it = 0
while True:
    x_ = x - 0.1 * f(x)
    num_of_it += 1
    if abs(x - x_) < err:
        print(x, f(x), num_of_it)
        break
    x = x_

print('метод Ньтона')
x = x_s
num_of_it = 0
while True:
    x_ = x - (1/fp(x)) * f(x)
    num_of_it += 1
    if abs(x - x_) < err:
        print(x, f(x), num_of_it)
        break
    x = x_
