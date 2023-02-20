import numpy as np
from sympy import *

x = Symbol("x")
f = x ** 2 * ln(x)
f = lambdify(x, f)

a = eval(input())
b = eval(input())
n = eval(input())

R = np.zeros((n + 1, n + 1))

delta_x = b - a

R[0][0] = (delta_x / 2) * (f(b) + f(a))

for i in range(1, n + 1):

    summation = 0

    for k in range(1, pow(2, i)):

        summation = summation + f(a + k * (delta_x / 2))
    
    R[i][0] = (1 / 2) * (delta_x / 2) * (f(a) + 2 * summation + f(b))

    delta_x = delta_x / 2

for i in range(1, n + 1):

    for j in range(1, i + 1):

        R[i][j] = R[i][j - 1] + ((R[i][j - 1] - R[i - 1][j - 1]) / (pow(4, j) - 1))

print(np.round(R, 5))