import numpy as np
from sympy import *

degree = eval(input())

for i in range(0, degree + 1):

    coeffecient = np.zeros(degree + 1)

    coeffecient[i] = eval(input())

x0 = eval(input())

y = coeffecient[degree - 1]
z = coeffecient[degree - 1] * degree

for j in range(degree - 1, 0, -1):

    y = x0 * y + coeffecient[j]
    z = x0 * z + y

y = x0 * y + coeffecient[0]

print(y, z)