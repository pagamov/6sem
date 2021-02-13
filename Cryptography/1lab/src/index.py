from math import *
from random import randint
import liba
# n = 160769357899975610828199539114109518167531134514190990785144666932076614717841
# n = 160769357899975610828199539114109518167531134514190990785144666932076614717841

# NOTE: 497293 = 509 * 977 primes
# n = 497293
n = 539873
B = 19
# NOTE 1: find sqrt of n and floor up
start = int(floor(n**(2**-1)) + 1)
print "start", start
# NOTE 2: find all primes <= B
primes = liba.find_primes(B)
print "primes under", B, "are", primes
# NOTE 3: find N such N^2 mod n are smooth under B
smooth_numbers = []
matrix = liba.Matrix_solver(primes)
while len(smooth_numbers) < 4:
    piv = liba.smooth_under((start**2) % n, primes)
    if piv != None:
        matrix.add(piv)
        smooth_numbers.append([start, (start**2) % n, piv])
        print start, (start**2) % n, piv
        # NOTE: make gauss matrix for solve
        gaus = liba.Gauss_Jordane(matrix, primes)
        # NOTE: solve gauss matrix mod 2 delete ban solves
        solving = gaus.solve(matrix.ban)
        # NOTE: check solves make addition for ban list
        solve, ban = gaus.chech()
        matrix.update_ban(ban)
        print solve
    start += 1

# NOTE 4: make matrix from smooth numbers
# matrix = liba.make_matrix_smooth(smooth_numbers, primes)

gaus = liba.Gauss_Jordane(matrix, primes)


print "solve", solving








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
