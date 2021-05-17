import copy
# make new error func base on matrix

A = [[26,-9,-8,8], [9,-21,-2,8], [-3,2,-18,8], [1,-6,-1,11]]
b = [20,-164,140,-81]
err = 10**-4

def display(m,t):
    """
    display matrix row by row and print text t before it
    """
    print(t)
    for row in m:
        print(row)
    print('')
def error(x,x_, err):
    if x_[0] == None:
        return False
    res = [0] * len(x)
    for i in range(len(x)):
        res[i] = abs(x[i] - x_[i])
    if max(res) > err:
        return False
    else:
        return True
def solve(A, b, err):
    x_ = [None] * len(A)
    x = [0] * len(A)
    num_of_it = 0

    while True:
        for i in range(len(A)):
            s = 0
            for j in range(len(A)):
                if i != j:
                    s += A[i][j] * x[j]
            x_[i] = (b[i] - s) / A[i][i]
        num_of_it += 1
        if error(x,x_,err):
            break
        x = copy.copy(x_)

    return x_, num_of_it
def prove(A, x):
    n = len(A)
    res = [0] * n
    for i in range(n):
        for j in range(n):
            res[i] += A[i][j] * x[j]
    return res

display(A,'matrix A')
display([b],'b vector')
x, it = solve(A, b, err)
display([x], 'solve')
display([it], 'num_of_it')
display([prove(A, x)], 'prove for x')
