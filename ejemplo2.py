import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return y - t**2 + 1

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
b = 2
n = 100
h = (b - a) / n

grid = np.linspace(a,b,n+1)
t = np.linspace(a,b,n+1)
y = np.zeros(n+1)
y[0] = 0.5

exact = t**2 + 2*t + 3 - (5/2)*np.exp(t)

y_euler = euler(t,y,h,n)

plt.plot(t,y_euler,"r",label="Euler")
# plt.plot(t,euler_modificado(t,y,h,n),"b",label="Euler mod.")
# plt.plot(t,euler_implicito(t,y,h,n),"g",label="Euler imp.")
plt.plot(grid,exact,"k",lw=2)
plt.legend()
plt.show()



