import numpy as np
from sympy import *

a = eval(input())
b = eval(input())
n = eval(input())      

delta_x = (b - a) / n

x = Symbol("x")
f = x ** 2 * ln(x)
f = lambdify(x, f)

summation = 0

result = np.zeros(n)

for i in range(1, n):

    x_i = a + i * delta_x

    summation = summation + f(x_i)

    approximation = (delta_x / 2) * (f(a) + 2 * summation + f(b))

for i in range(0, n):
    
    result[i] = approximation

print(result)