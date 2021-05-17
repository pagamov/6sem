import copy
import math

# task run bigger matrix and remove Gram_Schmidt!
# run complex matrix... 

A = [[-4,-6,-3],[-1,5,-5],[6,2,5]]
# A = [[3,-7,-1],[-9,-8,7],[5,2,2]]
err = 10**-4

# λ_1≈7,112
# λ_2≈-0,556-3,821*i
# λ_3≈-0,556+3,821*i

def display(m,t):
    """
    display matrix row by row and print text t before it
    """
    print(t)
    n = 3
    template = '{:.' + str(n) + 'f}'
    for row in m:
        for num in row:
            print('('+str(template.format(num[0]))+','+str(template.format(num[1])), end=') ')
        print()
    print('')
def make_im(A):
    res = copy.deepcopy(A)
    for i in range(len(A)):
        for j in range(len(A)):
            res[i][j] = [res[i][j],0]
    return res
def transpose(A):
    res = copy.deepcopy(A)
    for i in range(len(A)):
        for j in range(len(A)):
            res[i][j] = A[j][i]
    return res
def mult(a,b):
    return [a[0]*b[0] - a[1]*b[1],a[0]*b[1] + a[1]*b[0]]
def div(a,b):
    r = mult(a,[b[0],-b[1]])
    d = b[0]*b[0] + b[1]*b[1]
    return [r[0]/d,r[1]/d]
def proj(a, b):
    a_b = [0,0]
    b_b = [0,0]
    for i in range(len(a)):
        a_b[0] += mult(a[i],b[i])[0]
        a_b[1] += mult(a[i],b[i])[1]
        b_b[0] += mult(b[i],b[i])[0]
        b_b[1] += mult(b[i],b[i])[1]
    # a_b/b_b
    k = div(a_b,b_b)
    res = copy.deepcopy(b)
    for i in range(len(b)):
        res[i] = mult(k, b[i])
    return res
def sub_v(a,b):
    res = copy.deepcopy(a)
    for i in range(len(a)):
        res[i][0] = a[i][0] - b[i][0]
        res[i][1] = a[i][1] - b[i][1]
    return res
def normalize(A):
    res = copy.deepcopy(A)
    for j in range(len(A)):
        s = [0,0]
        for i in range(len(A)):
            s[0] += mult(A[i][j], A[i][j])[0]
            s[1] += mult(A[i][j], A[i][j])[1]
        s[0] = math.sqrt(s[0])
        if s[1] != 0:
            print('LOL')
            exit()
        for i in range(len(A)):
            res[i][j] = div(A[i][j],s)
    return res
def Gram_Schmidt(A):
    A = transpose(A)
    b = []
    for i in range(len(A)):
        curr = copy.deepcopy(A[i])
        for j in range(len(b)):
            curr = sub_v(curr, proj(curr, b[j]))
        b.append(copy.deepcopy(curr))
    return normalize(transpose(b))
def m_zero(n):
    res = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append([0,0])
        res.append(r)
    return res
def prois(A, B):
    R = m_zero(len(A))
    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)):
                R[i][j][0] += mult(A[i][k],B[k][j])[0]
                R[i][j][1] += mult(A[i][k],B[k][j])[1]
    return R
def error(A, err):
    er = []
    for i in range(1,len(A)):
        er.append(A[i][0][0])
    if max(er) < err:
        return True
    return False
def solve(A):
    res = [[A[0][0][0],0]]
    x = A[1][1][0]
    y = A[2][2][0]
    z = A[1][2][0] * A[2][1][0]
    D = (x+y)*(x+y)-4*(x*y-z)
    res.append([(x+y)/2, math.sqrt(-D)/2])
    res.append([(x+y)/2, -math.sqrt(-D)/2])
    return res

A = make_im(A)
display(A, 'A matrix')
display(prois(Gram_Schmidt(A), prois(transpose(Gram_Schmidt(A)),A)),'Q*R matrix')

num_of_it = 0
while True:
    Q = Gram_Schmidt(A)
    R = prois(transpose(Q),A)
    A = prois(R,Q)
    num_of_it += 1
    if error(A,err):
        display(A, 'res')
        print('num_of_it',num_of_it)
        display([solve(A)], 'self numbers')
        break
