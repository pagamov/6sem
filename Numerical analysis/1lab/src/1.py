import copy

A = [[-1,-7,-3,-2],
     [-8,1,-9,0],
     [8,2,-5,-3],
     [-5,3,5,-9]]

b = [-12,-60,-91,-43]

def display(m,t):
    """
    display matrix row by row and print text t before it
    """
    print(t)
    for row in m:
        print(row)
    print('')
def m_zero(n):
    res = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append(0)
        res.append(r)
    return res
def Gaus(A):
    U = copy.deepcopy(A)
    L = m_zero(len(A))
    n = len(A)
    for i in range(n):
        for j in range(n):
            if i == j:
                L[i][j] = 1

    for i in range(n-1):
        for j in range(i+1, n):
            do_d = (-U[j][i]) / U[i][i]
            for k in range(i, n):
                U[j][k] = U[i][k] * do_d + U[j][k]


        display(U, 'm')
def LU(A):
    U = copy.deepcopy(A)
    L = m_zero(len(A))
    n = len(A)

    for i in range(n):
        for j in range(i,n):
            L[j][i] = U[j][i] / U[i][i]

    for k in range(1,n):
        for i in range(k-1,n):
            for j in range(i,n):
                L[j][i] = U[j][i] / U[i][i]
        for i in range(k,n):
            for j in range(k-1,n):
                U[i][j] = U[i][j] - L[i][k-1] * U[k-1][j]

    return L,U
def prois(U, L):
    n = len(U)
    R = m_zero(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                R[i][j] += L[i][k] * U[k][j]
    return R
def determinant_recursive(A, total=0):
    """
    find determinant of matrix
    """
    # Section 1: store indices in list for row referencing
    indices = list(range(len(A)))
    # Section 2: when at 2x2 submatrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    # Section 3: define submatrix for focus column and call this function
    for fc in indices: # A) for each focus column, ...
        # find the submatrix ...
        As = copy.deepcopy(A) # B) make a copy, and ...
        As = As[1:] # ... C) remove the first row
        height = len(As) # D)
        for i in range(height):
            # E) for each remaining row of submatrix ...
            #     remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc+1:]
        sign = (-1) ** (fc % 2) # F)
        # G) pass submatrix recursively
        sub_det = determinant_recursive(As)
        # H) total all returns from recursion
        total += sign * A[0][fc] * sub_det
    return total
def transposeMatrix(m):
    return list(map(list,zip(*m)))
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant
def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors
def solve_L(L, b):
    n = len(L)
    y = [0] * n
    for i in range(n):
        s = 0
        for p in range(i):
            s += L[i][p] * y[p]
        y[i] = b[i] - s
    return y
def solve_U(U, y):
    n = len(U)
    x = [0] * n
    for i in range(n):
        s = 0
        for p in range(i-1):
            s += U[n-1-i][n-p-1] * x[n-p-1]
        x[n-i-1] = (y[n-i-1] - s) / U[n-i-1][n-i-1]

    for i in range(n):
        s = 0
        for p in range(n-i,n):
            s += U[n-i-1][p] * x[p]
        x[n-i-1] = (y[n-i-1] - s) / U[n-i-1][n-i-1]
    return x
def prove(A, x):
    n = len(A)
    res = [0] * n
    for i in range(n):
        for j in range(n):
            res[i] += A[i][j] * x[j]
    return res

display(A, "A matrix")
display([b], "b vector")
L,U = LU(A)
display(U, "U matrix")
display(L, "L matrix")
display(prois(U, L), "R mult of L and U")
print('det of A', determinant_recursive(A))
print('det L * det U', determinant_recursive(L) * determinant_recursive(U))
inv = getMatrixInverse(A)
display(inv, 'invert matrix A')
# inv_U = getMatrixInverse(U)
# inv_L = getMatrixInverse(L)
# inv_LU = prois(inv_U, inv_L)
# display(inv_LU, 'invert matrix LU')
y = solve_L(L, b)
display([y], 'solve for L')
x = solve_U(U, y)
display([x], 'solve for U')
display([prove(A,x)], 'prove for A')
