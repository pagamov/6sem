from time import time

def gcd(a,b):
    if a == 0:
        return 0,1,b
    x1,y1,_ = gcd(b%a,a)
    x = y1 - (b//a) * x1
    y = x1
    return x,y,b
def sqr(n):
    if n == 0:
        return 0
    x = n
    prev = x
    while True:
        x = (x + n // x) // 2;
        if prev == x or (x + n // x) // 2 == x + 1:
            break
        else:
            prev = x
    return x
def c_mod(a,p):
    res = a % p
    if res < 0:
        print('lol clever!')
    if res >= 0:
        return res
    else:
        return p + res
def rev(a,b):
    if a == b:
        print('rev err')
        exit()
    x,y,_ = gcd(a,b)
    return c_mod(x,b)

if __name__ == "__main__":
    # A,B,P = 7,4,17
    A,B,P = 1487,227,70997
    t = time()
    points = []
    dots = []
    if (4 * A * A * A + 27 * B * B) % P == 0:
        print('error')
        exit()
    y_get,y,order = 0,0,1
    for x in range(P):
        y_get = c_mod((x**3 + A*x + B), P)
        for y in range(sqr(y_get),P):
            if (y*y) % P == y_get:
                if not order-1:
                    points.append([x,y])
                dots.append([x,y])
                time_need = 100 * (time() - prev_t[0]) / ((y + x*P)/(P*P)*100) / 60
                print('\r'+str(y + x*P)+'/'+str(P*P)+' '+'{0:.2f}'.format((y + x*P)/(P*P)*100)+' % need time: '+'{0:.2f}'.format(time_need)+' min',end='')
                order += 1
    print()
    print('order',order)
    min = order
    count = 1
    for i in points:
        s,p = [i[0],i[1]],[i[0],i[1]]
        print('working with', s)
        while s[1] != 0:
            if s == [p[0],P-p[1]]:
                s = [0,0]
            elif s == p:
                m = c_mod(c_mod((3 * s[0] * s[0])%P+A,P)*rev((2*s[1])%P,P),P)
                x_new = c_mod((m*m)%P-(2*s[0])%P,P)
                s = [x_new, c_mod((m * c_mod(s[0] - x_new, P)) % P - s[1], P)]
            else:
                m = c_mod(c_mod(i[1] - s[1], P)*rev(c_mod(i[0]-s[0],P),P),P)
                x_new = c_mod((m * m) % P - s[0] - i[0], P)
                s = [x_new, c_mod((m * c_mod(s[0] - x_new, P)) % P - s[1], P)]
            count += 1
        if count < min:
            min = count
            if min == 1:
                break
        count = 1
    print('N =', min)
    print('total time','{0:.2f}'.format(time()-t), 'min')
    ex = input()
