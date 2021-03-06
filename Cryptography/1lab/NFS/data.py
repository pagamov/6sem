def eratosthenes(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n, number):
                numbers[candidate-2] = 0
    return list(filter(lambda x: x != 0, numbers))

def GCD(m,n):
    mult = 1
    while True:
        if m == 0 or n == 0 or m == n:
            return mult*max(n,m)
        if m == 1 or n == 1:
            return mult
        mm2 = m % 2
        nm2 = n % 2
        if mm2 == 0 and nm2 == 0:
            mult *= 2
            m = m//2
            n = n//2
        elif mm2 == 0 and nm2 != 0:
            m = m//2
        elif mm2 != 0 and nm2 == 0:
            n = n//2
        elif mm2 != 0 and nm2 != 0:
            if n > m:
                piv = (n-m)//2
                n = m
                m = piv
            elif n < m:
                m = (m-n)//2
class Q:
    def __init__(self,n):
        self.q = []
        d = 3
        self.d = d
        self.m = int(n**(1/d)) 
        while d > 0:
            d+=1
def makeQ(n):
    q = []
    k = 3
    m = int(n**(1/d))
    print("m chose", m)





def makeRFB(B):
    return eratosthenes(B)
def makeAFB(B):
    res = eratosthenes(B)

