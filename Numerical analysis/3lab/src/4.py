# done
import matplotlib.pyplot as plt

x = [0.0,0.1,0.2,0.3,0.4]
y = [1.0,1.1052,1.2214,1.3499,1.4918]

x_ans = 0.2

def find_start(x, p):
    for i in range(0, len(p) - 1):
        if p[i] <= x and x <= p[i + 1]:
            return i

def df1(x, y, x0):
    i = find_start(x0, x)
    elem1 =  (y[i + 1] - y[i]) / (x[i + 1] - x[i])
    elem2 =  ((y[i + 2] - y[i + 1]) / (x[i + 2] - x[i + 1]) - elem1) / (x[i + 2] - x[i]) * (2 * x0 - x[i] - x[i + 1])
    return elem1 + elem2

def df2(x, y, x0):
    i = find_start(x0, x)
    elem1 = (y[i + 2] - y[i + 1]) / (x[i + 2] - x[i + 1])
    elem2 = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
    return 2 * (elem1 - elem2) / (x[i + 2] - x[i])


print(df1(x, y, x_ans))

print(df2(x, y, x_ans))

plt.plot(x,y)
plt.scatter(x_ans,y[2])
plt.show()
