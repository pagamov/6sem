def Factor(n, B):
    from time import time
    import decimal,copy
    from Primes import Primes
    from Matrix_solver import Matrix_solver
    from lib import smooth_under,perm_find,GCD,Q,smooth_region,eratosthenes


    # mat = Matrix_solver([2,3,5,7])
    # mat.add([0,0,0,1])
    # mat.add([0,1,1,1])
    # mat.add([0,0,0,1])
    # mat.add([1,1,0,1])
    # mat.add([1,1,0,0])
    # ans = mat.solve()
    # print ans
    # exit()

    start = long(decimal.Decimal(n).sqrt() + 1)
    q = Q(n)
    primes = Primes(n,B,q)
    print "primes len", len(primes)
    smooth_numbers = []
    matrix = Matrix_solver(primes.p)
    step = 10**5
    k = 1
    smooth_numbers = []
    # while (k-1)*step < start:
    while True:
        ans = smooth_region((k-1)*step,k*step,q,primes)
        print len(ans),(k-1)*step,k*step
        for i in range(len(ans)):
            smooth_numbers.append([ans[i][0],ans[i][1],ans[i][2]])
            matrix.add(ans[i][2])
        ans = smooth_region(-k*step,-(k-1)*step,q,primes)
        print len(ans),-k*step,-(k-1)*step
        for i in range(len(ans)):
            smooth_numbers.append([ans[i][0],ans[i][1],ans[i][2]])
            matrix.add(ans[i][2])
        k+=1
        if len(smooth_numbers) > len(primes):
            solve = matrix.solve()
            print "solve found"
            for s in solve:
                # print s
                left = 1
                right = []
                for i in s:
                    left *= start + smooth_numbers[i][0]
                    right.append(smooth_numbers[i][2])
                true_right = 1
                right_piv = [0] * len(primes)
                for r in right:
                    for j in range(len(primes)):
                        right_piv[j] += r[j]
                for j in range(len(right_piv)):
                    right_piv[j] /= 2
                for j in range(len(right_piv)):
                    true_right *= primes(j)**right_piv[j]
                # print "try gcd"

                # print left, true_right
                # left = abs(left)
                # true_right = abs(true_right)
                gcd = min(GCD(abs(left+true_right), n), GCD(abs(left-true_right), n))
                if gcd > 1 and n / gcd * gcd == n:
                    return [gcd, n/gcd]
    return [None, None]
