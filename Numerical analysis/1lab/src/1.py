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
    print t
    for row in m:
        print row
    print ''

display(A, "A matrix")
display([b], "b vector")

def m_zero(n):
    res = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append(0)
        res.append(r)
    return res

def LU(A):
    U = copy.deepcopy(A)
    L = m_zero(len(A))
    n = len(A)

    for i in range(n):
        for j in range(i,n):
            L[j][i]=U[j][i] / U[i][i]

    for k in range(1,n):
        for i in range(k-1,n):
            for j in range(i,n):
                L[j][i] = U[j][i] / U[i][i]
        for i in range(k,n):
            for j in range(k-1,n):
                U[i][j] = U[i][j] - L[i][k-1] * U[k-1][j]

    return L,U

L,U = LU(A)
display(U, "U matrix")
display(L, "L matrix")

def prois(U, L):
    n = len(U)
    R = m_zero(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                R[i][j] += L[i][k] * U[k][j]
    return R

R = prois(U, L)
display(R, "R mult of L and U")

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

print 'det of A', determinant_recursive(A)

print 'det L * det U', determinant_recursive(L) * determinant_recursive(U)

def invert(A):
    pass
