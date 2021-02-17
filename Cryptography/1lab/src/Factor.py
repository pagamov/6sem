def Factor(n, B):
    from time import time
    import decimal,copy
    from Primes import Primes
    from Matrix_solver import Matrix_solver
    from lib import smooth_under,perm_find,GCD,Q,smooth_region,eratosthenes

    start = long(decimal.Decimal(n).sqrt() + 1)
    q = Q(n)
    primes = Primes(n,B,q)
    print len(primes.p)
    smooth_numbers = []
    matrix = Matrix_solver(primes)
    # t = time()
    # ansl = 0
    # for ran in range(0,1000000,10000):
    #     ans = smooth_region(ran,ran+10000,q,primes)
    #     ansl += len(ans)
    #
    # print ansl, time() - t
    # t = time()
    # ans = []
    # # primes = eratosthenes(B)
    # print len(primes)
    # for i in range(0,1000000):
    #     piv = smooth_under(q(i), primes.p)
    #     if piv != None:
    #         ans.append(piv)
    # print len(ans), time() - t
    # exit()

    step = 10**3
    x = 0
    k = 1

    smooth_numbers = []
    while True:
        ans = smooth_region(x+((k-1)*step),x+(k*step),q,primes)
        print len(ans),x+((k-1)*step),x+(k*step)
        smooth_numbers += ans
        for i in range(len(ans)):
            matrix.add(ans[i][2])
        ans = smooth_region(x-(k*step),x-((k-1)*step),q,primes)
        print len(ans),x-(k*step),x-((k-1)*step)
        smooth_numbers += ans
        for i in range(len(ans)):
            matrix.add(ans[i][2])
        k+=1

        if len(smooth_numbers) > 0:
            solve = perm_find(matrix.solve(),0)
            print "perm found"
            for s in solve:
                left = 1
                right = []
                for i in range(len(s)):
                    if s[i] == 1:
                        left *= smooth_numbers[i][0]
                        right.append(copy.copy(smooth_numbers[i][2]))
                true_right = 1
                right_piv = [0] * len(primes)
                for r in right:
                    for j in range(len(primes)):
                        right_piv[j] += r[j]
                for j in range(len(right_piv)):
                    right_piv[j] = right_piv[j] / 2
                for j in range(len(right_piv)):
                    true_right *= primes(j)**right_piv[j]
                gcd = min(GCD(left+true_right, n), GCD(left-true_right, n))
                if gcd > 1 and n / gcd * gcd == n:
                    return [gcd, n/gcd]
    return [None, None]
