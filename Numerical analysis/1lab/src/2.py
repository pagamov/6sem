A = [[-14,-6],[-9,15,-1],[1,-11,1],[-7,12,3],[6,-7]]
b = [-78,-73,-38,77,91]

def display(m,t):
    """
    display matrix row by row and print text t before it
    """
    print(t)
    for row in m:
        print(row)
    print('')
def solve(m, b):
    y = [None] * len(m)
    alpha = [None] * len(m)
    beta = [None] * len(m)
    for i in range(len(m)):
        if i == 0:
            y[i] = m[i][0]
            alpha[i] = -1 * m[i][1] / y[i]
            beta[i] = b[i] / y[i]
        elif i == len(m) - 1:
            y[i] = m[i][1] + m[i][0] * alpha[i-1]
            beta[i] = (b[i] - m[i][0] * beta[i-1]) / y[i]
        else:
            y[i] = m[i][1] + m[i][0] * alpha[i-1]
            alpha[i] = -1 * m[i][2] / y[i]
            beta[i] = (b[i] - m[i][0] * beta[i-1]) / y[i]
    x = [0] * len(m)
    for i in range(len(m)):
        if i == 0:
            x[len(m)-i-1] = beta[len(m)-i-1]
        else:
            x[len(m)-i-1] = alpha[len(m)-i-1] * x[len(m)-i] + beta[len(m)-i-1]
    return x
def make_trig_matrix(A):
    m = []
    for i in range(len(A)):
        m.append([0]*len(A))
    for i in range(len(A)):
        if i == 0:
            m[i][0] = A[i][0]
            m[i][1] = A[i][1]
        elif i == len(A)-1:
            m[i][i-1] = A[i][0]
            m[i][i] = A[i][1]
        else:
            m[i][i-1] = A[i][0]
            m[i][i] = A[i][1]
            m[i][i+1] = A[i][2]
    return m
def prove(A, x):
    n = len(A)
    res = [0] * n
    for i in range(n):
        for j in range(n):
            res[i] += A[i][j] * x[j]
    return res

x = solve(A,b)
display(make_trig_matrix(A),'trig matrix')
display([b],'b vector')
display([prove(make_trig_matrix(A),x)], 'prove for x')
