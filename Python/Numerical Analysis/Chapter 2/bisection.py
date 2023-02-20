import numpy as np
from sympy import *

a = eval(input())
b = eval(input())
tolerance = eval(input())

x = Symbol("x")
f = x ** 3 + 4 * x ** 2 - 10

counter = 1

if(f.subs(x, a) * f.subs(x, b) < 0):

    p = (a + b) / 2

    print(counter, p, f.subs(x, p))

    while(abs(f.subs(x, p)) > tolerance):

        if(f.subs(x, a) * f.subs(x, p) < 0):

            b = p
        
        elif(f.subs(x, p) * f.subs(x, b) < 0):

            a = p

        p = (a + b) / 2

        counter = counter + 1

        print(counter, p, f.subs(x, p))
        
else:

    print("failed")