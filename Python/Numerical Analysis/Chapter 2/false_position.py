import numpy as np
from sympy import *

a = eval(input())
b = eval(input())
tolerance = eval(input())

x = Symbol("x")
f = cos(x) - x

counter = 0

while(True):

    slope = (f.subs(x, a) - f.subs(x, b)) / (a - b)

    if(abs(slope) < tolerance):

        continue

    p = b - f.subs(x, b) / slope

    if(f.subs(x, a) * f.subs(x, p) < 0):

        b = p

    elif(f.subs(x, b) * f.subs(x, p) < 0):

        a = p

    counter = counter + 1

    print(counter + 1, p, f.subs(x, p))

    if(abs(f.subs(x, p)) < tolerance):

        break

else:

    print("failed")