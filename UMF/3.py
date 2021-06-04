import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm
from math import exp, sin, cos
import numpy as np

l1 = 1
l2 = 1
pi = 3.14

def f(x,y):
    n = 2
    res = 0
    while n < 5:
        up1 = 2*n*(cos(pi*n)+1)*(exp((pi*n/l2)*x) - exp(2*(pi*n/l2)*l1 - (pi*n/l2)*x))
        down1 = pi*(n**2-1)*(pi*n/l2)*(exp((pi*n/l2)*x) + exp(2*(pi*n/l2)*l1 - (pi*n/l2)*x))
        up2 = 10*(1 - cos(pi*n))*(exp((pi*n/l2)*x) + exp(-1*(pi*n/l2)*x))
        down2 = l2 * (pi*n/l2)**2 * (exp((pi*n/l2)*l1) - exp(-1*(pi*n/l2)*l1))
        res += (up1/down1 + up2/down2) * sin((pi*n/l2)*y)
        n += 1
    return res

def get_data(lx,ly):
    xr,yr,zr = [],[],[]
    step = 0.1
    x = 0
    while x <= lx:
        y = 0
        while y <= ly:
            xr.append(x)
            yr.append(y)
            # zr.append(f(x,y))
            y += step
        x += step
    return xr,yr,zr

xs,ys,zs = get_data(l1,l2)


# xs = [1,2,3]
# ys = [4,5]

X,Y = np.meshgrid(xs, ys)
Z = np.array([[f(x,y) for y in ys] for x in xs])




fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(1, 1, 1, projection='3d')


# ax.plot_surface(X,Y,Z)

# set up a figure twice as wide as it is tall


#===============
#  First subplot
#===============
# set up the axes for the first plot


# plot a 3D surface like in the example mplot3d/surface3d_demo
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
fig.colorbar(surf, shrink=4, aspect=10)

#===============
# Second subplot
#===============
# set up the axes for the second plot
# ax = fig.add_subplot(1, 2, 2, projection='3d')

# plot a 3D wireframe like in the example mplot3d/wire3d_demo
# X, Y, Z = get_test_data(0.05)
# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()
