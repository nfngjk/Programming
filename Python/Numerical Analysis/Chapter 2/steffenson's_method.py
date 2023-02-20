import numpy as np
from sympy import *

x = Symbol("x")
f = sqrt((10 / (x + 4)))
f = lambdify(x, f)

p0 = eval(input())
tolerance = eval(input())

counter = 0

p1 = f(p0)
p2 = f(p1)

p_i = p0 - ((p1 - p0) ** 2 / (p2 - 2 * p1 + p0))

while(True):

    if(abs(p_i - p0) < tolerance):

        print(counter, p0, p1, p2)

        break

    print(counter, p0, p1, p2)

    p0 = p_i

    counter = counter + 1

else:

    print("failed")