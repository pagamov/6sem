def Factor(n, B):
    from time import time
    import decimal,copy
    from Primes import Primes
    from Matrix_solver import Matrix_solver
    from lib import smooth_under,perm_find,GCD,Q,smooth_region,eratosthenes
    start = long(decimal.Decimal(n).sqrt() + 1)
    q = Q(n)
    primes = Primes(n,B,q)
    print "primes len", len(primes)
    smooth_numbers = []
    matrix = Matrix_solver(primes.p)
    step = 10**4
    k = 1
    smooth_numbers = []
    while q((k-1)*step) < n:
        ans = smooth_region((k-1)*step,k*step,q,primes)
        print len(ans),(k-1)*step,k*step
        for i in range(len(ans)):
            smooth_numbers.append([ans[i][0],ans[i][1],ans[i][2]])
            matrix.add(ans[i][2])

        exit()
        ans = smooth_region(-k*step,-(k-1)*step,q,primes)
        print len(ans),-k*step,-(k-1)*step
        for i in range(len(ans)):
            smooth_numbers.append([ans[i][0],ans[i][1],ans[i][2]])
            matrix.add(ans[i][2])
        k+=1
        if len(smooth_numbers) > len(primes):
            solve = matrix.solve()
            # print "solve found"
            if len(solve) > 0:
                print "\n\t***********\n\t\tYaaaaaaaaaay :)))))\n\t***********\n"
            for s in solve:
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
                gcd = min(GCD(abs(left+true_right), n), GCD(abs(left-true_right), n))
                if gcd > 1 and n / gcd * gcd == n:
                    return [gcd, n/gcd]
    return [None, None]
