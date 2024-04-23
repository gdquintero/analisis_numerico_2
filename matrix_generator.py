import numpy as np
import pandas as pd
import random

n = 10

A = np.zeros((n,n))
B = np.zeros((n,n))

random.seed(5)

for i in range(n):
    for j in range(n):
        if i >= j:
            A[i,j] = random.random() + 1

for i in range(n):
    for j in range(n):
        if i <= j:
            B[i,j] = random.random() + 1

np.savetxt("inferior.txt",A)
np.savetxt("superior.txt",B)
