import numpy as np
from sympy import *

a = eval(input())
b = eval(input())
n = eval(input())           # n is an even number

delta_x = (b - a) / (n + 1)

x = Symbol("x")
f = x ** 2 * ln(x ** 2 + 1)
f = lambdify(x, f)

summation = 0

result = np.zeros(n)

for i in range(-1, n + 2):

    x_i = (1 / 2) * (a * ((i + 1) / (n + 1)) + b * ((2 * n + 1 - i) / (n + 1)))  

    if(i % 2 == 0):

        summation = summation + f(x_i)

    approximation = summation * delta_x

for i in range(0, n):

    result[i] = approximation

print(result)