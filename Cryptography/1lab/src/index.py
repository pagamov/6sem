from math import *
from fractions import gcd
from random import randint
import liba
import copy
import decimal
# n = 160769357899975610828199539114109518167531134514190990785144666932076614717841
# n = 1250171497372227982026555999675170108947918951378367343470923483104158597216632066586300921566811265776465427395026458151240042366061271512107752586681699923914902061886213022544496783070727061083763996630816279869169194623169255711135422521925444135939014878277515299870536875962948267973899545621728547726545192382593936985574978881305949487523233148677106330650818223443955800622774189936635106363035784698216185461573761714766211607812695281252356674432444279
B = 19
n = 23687 * 12613
# NOTE 1: find sqrt of n and floor up
start = long(decimal.Decimal(n).sqrt() + 1)
print "start", start
# NOTE 2: find all primes <= B
primes = liba.eratosthenes(B)
print "primes done", len(primes)
# NOTE 3: find N such N^2 mod n are smooth under B
smooth_numbers = []
matrix = liba.Matrix_solver(primes)
while True:
    piv = liba.smooth_under((start**2) % n, primes)
    if piv != None:
        matrix.add(piv)
        smooth_numbers.append([start, (start**2) % n, piv])
        # NOTE: make gauss matrix for solve
        gaus = liba.Gauss_Jordane(matrix, primes)
        # NOTE: solve gauss matrix mod 2 delete ban solves
        solving = gaus.solve(matrix.ban)
        # print "gauss matrix", str(len(gaus.matrix)) + "x" + str(len(gaus.matrix[0]))
        # NOTE: check solves make addition for ban list
        solve, ban = gaus.check(solving)
        print "b", ban
        matrix.update_ban(ban)
        if len(solve) != 0:
            for s in solve:
                left = []
                right = []
                for i in range(len(s)):
                    if s[i] == 1:
                        left.append(smooth_numbers[i][0])
                        right.append(copy.copy(smooth_numbers[i][2]))

                true_left = 1
                for i in left:
                    true_left *= i

                true_right = 1
                if len(right) != 0:
                    right_piv = [0] * len(primes)
                    for r in right:
                        for j in range(len(primes)):
                            right_piv[j] += r[j]
                    for j in range(len(right_piv)):
                        right_piv[j] = right_piv[j] / 2
                    for j in range(len(right_piv)):
                        true_right *= primes[j]**right_piv[j]

                gcd = min(liba.GCD(true_left+true_right, n), liba.GCD(true_left-true_right, n))
                if gcd > 1:
                    if n / gcd * gcd == n:
                        print "ANS", gcd , n/gcd, n
                        exit()
    # start += randint(1,10)
    start += 1

# NOTE 4: make matrix from smooth numbers
# matrix = liba.make_matrix_smooth(smooth_numbers, primes)

# gaus = liba.Gauss_Jordane(matrix, primes)
#
#
# print "solve", solving








#
# # NOTE 1: pick d >= 3
# d = 3
#
# # NOTE 2.1: get m : [n^(1/(d+1))] < m < [n^(1/d)]
# low_bound = floor(n**((d+1)**-1))
# print "low", int(low_bound)
#
# up_bound = floor(n**(d**-1))
# print "up", int(up_bound)
#
# m = randint(low_bound, up_bound)
# m = 35
# print "base", m
#
# # NOTE 2.2: make polinome from n on m base : 123,2 -> {1, 1, 1, 1, 0, 1, 1}
# def make_polinome(n, m):
#     res = []
#     piv = 0
#     while n > m:
#         piv = n / m
#         res.append(n - piv * m)
#         n = piv
#     res.append(piv)
#     return res
#
# polinome = make_polinome(n,m)
#
# print polinome
#
# # NOTE 3: make f_1(x) = x^d + a_{d-1}x^(d-1) + ... + a_0
# class f_1:
#     def __init__(self,polinome):
#         # self.m = m
#         self.polinome = []
#         for number in polinome:
#             self.polinome.append(number)
#
#     def __call__(self,x):
#         res = 0
#         i = 0
#         for number in self.polinome:
#             res += number * (x**i)
#             i += 1
#         return res
#
#
# f1 = f_1(polinome)
#
# # print f1.polinome
# # print f1(m) == n
#
# # NOTE 4: make F_1(a,b) = b^d * f_1(a/b)
# class F_1(f_1):
#     def __call__(self,a,b):
#         res = 0
#         i = 0
#         j = d
#         for number in self.polinome:
#             res += number * (a**i) * (b**j)
#             i += 1
#             j -= 1
#         return res
#
# F1 = F_1(polinome)
#
# # NOTE 5.1: f_2(x) = x - m
# class f_2:
#     def __call__(self,x):
#         return x - m
#
# f2 = f_2()
#
# # NOTE 5.2: F_2(a,b) = a - bm
# class F_2:
#     def __call__(self,a,b):
#         return a - b*m
#
# F2 = F_2()
#
# # NOTE 6: pick L_1 and L_2 as sieve region : SR = {1 <= b <= L_1, -L_2 <= a <= L_2}
# L1 = randint(m**(1/2),m)
# L2 = randint(m**(1/2),m)
#
# print "L1", L1
# print "L2", L2
