def Factor(n, B):
    from time import time
    import decimal,copy
    from Primes import Primes
    from Matrix_solver import Matrix_solver
    from lib import GCD,Q,smooth_region,eratosthenes
    from data import step
    from color import color
    q = Q(n)
    primes = Primes(n,B,q)
    smooth_numbers = []
    matrix = Matrix_solver(primes.p)
    print("step:",color(step,"data"))
    k = 1
    found_smooth = 0
    while q((k-1)*step) < n:
        ans = smooth_region((k-1)*step,k*step,q,primes)
        for i in range(len(ans)):
            smooth_numbers.append(ans[i])
            matrix.add(ans[i][2])
        ans = smooth_region(-k*step,-(k-1)*step,q,primes)
        for i in range(len(ans)):
            smooth_numbers.append(ans[i])
            matrix.add(ans[i][2])
        k+=1
        print("Total number of smooth numberes:",color(len(smooth_numbers),'data'))
        if len(smooth_numbers) > len(primes):
            print(color("All smooth numbers found",'strong')+'\n')
            solve = matrix.solve()

            left = 1
            right = []
            for i in solve:
                left *= int(decimal.Decimal(n).sqrt() + 1) + smooth_numbers[i][0]
                right.append(smooth_numbers[i][2])
            true_right = int(1)
            right_piv = [0] * len(primes)
            for r in right:
                for j in range(len(primes)):
                    right_piv[j] += int(r[j])
            for j in range(len(right_piv)):
                right_piv[j] //= 2
            for j in range(len(right_piv)):
                true_right *= int(primes(j)**right_piv[j])

            gcd = min(GCD(abs(int(left+true_right)), n), GCD(abs(int(left-true_right)), n))
            if gcd > 1 and n // gcd * gcd == n:
                print(color("Solve Done",'strong'))
                return [gcd, n//gcd]
    return [None, None]
