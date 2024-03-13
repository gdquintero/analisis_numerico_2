import math

x = float(input("Digite un numero real: "))

n_correcto = True

n = int(input("Digite numero de terminos: "))

while n_correcto:
    if n >= 0:
        n_correcto = False
    else:
        n = int(input("Numero incorrecto, digite un entero no negativo: "))

suma = 1

for k in range(1,n+1):
    suma += ((-1)**k) * (x**(2 * k)) / math.factorial(2 * k)

print(suma)

