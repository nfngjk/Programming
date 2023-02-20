import numpy as np
from sympy import *

x = np.array([8.3, 8.6])
y = np.array([17.56492, 18.50515])
y_prime = np.array([3.116256, 3.151762])

n = len(x)

z = np.zeros(2 * n + 1)

Q = np.zeros((2 * n, 2 * n + 1))

for i in range(0, n):

    Q[2 * i][0] = x[i]
    Q[2 * i + 1][0] = x[i]

    Q[2 * i][1] = y[i]
    Q[2 * i + 1][1] = y[i]
    
    Q[2 * i + 1][2] = y_prime[i]

    if(i != 0):

        Q[2 * i][2] = (Q[2 * i][1] - Q[2 * i - 1][1]) / (Q[2 * i][0] - Q[2 * i - 1][0])

for i in range(2, 2 * n):

    for j in range(2, i + 1):

        Q[i][j + 1] = (Q[i][j] - Q[i - 1][j]) / (Q[i][0] - Q[i - j][0])

for i in range(0, 2 * n):

    print(Q)