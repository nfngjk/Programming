import numpy as np
from sympy import *

p0 = eval(input())
tolerance = eval(input())

x = Symbol("x")
f = x ** 3 - 2 * x ** 2 - 5

counter = 0

while(True):

    df = diff(f, x)

    slope = df.subs(x, p0)

    if(abs(slope) < tolerance):

        continue

    p0 = p0 - f.subs(x, p0) / slope

    counter = counter + 1

    print(counter, p0, f.subs(x, p0))

    if(abs(f.subs(x, p0) / slope) < tolerance and abs(f.subs(x, p0)) < tolerance):

        break

else:

    print("failed")