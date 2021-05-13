from time import time

def clever_mod(a,p):
    res = a % p
    if res >= 0:
        return res
    else:
        return p + res

def gcd(a,b):
    if b > 0:
        return gcd(b, a % b)
    else:
        return a

def gcd(a,b,x,y): #???
    if a == 0:
        x = 0
        y = 1
        return x,y,b
    x1,y1,b1 = gcd(b%a,a,x,y)
    x = y1 - (b/a) * x1
    y = x1
    return x,y,b
