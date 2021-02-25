def Factor(n, B):
    import decimal
    from color import color

    # some functions to support functionality (LOL)
    from lib import GCD,Q
    q = Q(n)

    # class generating Factor base
    from Primes import Primes
    primes = Primes(n,B,q)

    # func to suive until we have critical len of smooth numbers
    from Suive import suive
    smooth_numbers = suive(q,primes)

    print("Total number of smooth numberes:",color(len(smooth_numbers),'data'))
    print(color("All smooth numbers found",'strong')+'\n')

    # matrix solves
    from Matrix_solver import Matrix_solver
    matrix = Matrix_solver(primes.p)

    for smooth in smooth_numbers:
        matrix.add(smooth[2])

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
