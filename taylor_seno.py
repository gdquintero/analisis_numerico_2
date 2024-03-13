import math

x = float(input("Digite un numero real: "))
epsilon = 1e-14

k = 0
suma = 0

while True:
    termino = x**(2*k + 1) / math.factorial(2*k + 1)
    suma += (-1)**k * termino

    if abs(termino) < epsilon:
        break

    k += 1

print(k,suma)

    