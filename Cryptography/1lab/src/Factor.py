def Factor(n, B):
    from time import time
    import decimal,copy
    from Primes import Primes
    from Matrix_solver import Matrix_solver
    from lib import GCD,Q,smooth_region,eratosthenes
    start = int(decimal.Decimal(n).sqrt() + 1)
    q = Q(n)
    primes = Primes(n,B,q)
    smooth_numbers = []
    matrix = Matrix_solver(primes.p)
    step = 10**4
    print("step " + '\033[95m' + str(step) + '\033[0m')
    k = 1
    smooth_numbers = []
    while q((k-1)*step) < n:
        ans = smooth_region((k-1)*step,k*step,q,primes)
        for i in range(len(ans)):
            smooth_numbers.append([ans[i][0],ans[i][1],ans[i][2]])
            matrix.add(ans[i][2])
        ans = smooth_region(-k*step,-(k-1)*step,q,primes)
        for i in range(len(ans)):
            smooth_numbers.append([ans[i][0],ans[i][1],ans[i][2]])
            matrix.add(ans[i][2])
        k+=1
        if len(smooth_numbers) > 0:
            solve = matrix.solve()
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
                    right_piv[j] = int(right_piv[j] / 2)
                for j in range(len(right_piv)):
                    true_right *= primes(j)**right_piv[j]
                gcd = min(GCD(abs(int(left+true_right)), n), GCD(abs(int(left-true_right)), n))
                if gcd > 1 and n / gcd * gcd == n:
                    print("\n\033[91m"+"Yaaaaaaaaaay :)))))"+"\033[0m")
                    return [gcd, n/gcd]
    return [None, None]
