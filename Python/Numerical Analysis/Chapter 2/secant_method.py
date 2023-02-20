import numpy as np
from sympy import *

a = eval(input())
b = eval(input())
tolerance = eval(input())

x = Symbol("x")
f = cos(x) - x

counter = 1

while(True):

    slope = (f.subs(x, a) - f.subs(x, b)) / (a - b)

    if(abs(slope) < tolerance):

        continue

    a = b
    b = b - f.subs(x, b) / slope

    counter = counter + 1

    print(counter, b, f.subs(x, b))

    if(abs(f.subs(x, b) / slope) < tolerance and abs(f.subs(x, b)) < tolerance):

        break

else:

    print("failed")