import numpy as np
from sympy import *

a = eval(input())
b = eval(input())
n = eval(input())           # n is an even number

delta_x = (b - a) / n

x = Symbol("x")
f = x
f = lambdify(x, f)

x_odd = 0
x_even = 0

result = np.zeros(n)

for i in range(1, n):

    x_i = a + i * delta_x

    if(i % 2 == 0):

        x_even = x_even + f(x_i)

    else:

        x_odd = x_odd + f(x_i)

    approximation = (delta_x / 3) * (f(a) + 4 * x_odd + 2 * x_even + f(b))

for i in range(0, n):

    result[i] = approximation

print(result)