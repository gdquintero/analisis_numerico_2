import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return np.exp(2 * t) * y 

def euler(t,y,h,n):
    for k in range(n):
        phi = f(t[k],y[k])
        y[k+1] = y[k] + h * phi
    
    return y

def euler_modificado(t,y,h,n):
    for k in range(n):
        k1 = f(t[k],y[k])
        k2 = f(t[k] + h,y[k] + h * k1)
        phi = 0.5 * (k1 + k2)
        y[k+1] = y[k] + h * phi

    return y

def euler_implicito(t,y,h,n):
    for k in range(n):
        y[k+1] = y[k] / (1 - h * np.exp(2 * (t[k] + h)))

    return y

a = 0
b = 1
n = 10
h = (b - a) / n
grid = np.linspace(a,b,1000)
t = np.linspace(0,1,n+1)
y = np.zeros(n+1)
y[0] = 1

exact = np.exp((np.exp(2 * grid) - 1) / 2)

plt.plot(grid,exact,"k")
plt.plot(t,euler(t,y,h,n),"r")
plt.plot(t,euler_modificado(t,y,h,n),"b")
plt.plot(t,euler_implicito(t,y,h,n))
plt.show()


