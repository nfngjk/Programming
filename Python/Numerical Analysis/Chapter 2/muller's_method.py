from sympy import *
import numpy as np

x = Symbol("x")
f = x ** 4 - 3 * x ** 3 + x ** 2 + x + 1
f = lambdify(x, f)

x0 = eval(input())
x1 = eval(input())
x2 = eval(input())

tolerance = eval(input())

counter = 0

while(abs(f(x2)) > tolerance):

    A = np.array([[1, x0, x0 ** 2], [1, x1, x1 ** 2], [1, x2, x2 ** 2]])
    B = np.array([f(x0), f(x1), f(x2)])
    
    vector_x = np.linalg.solve(A, B)            # solve Ax = B
    
    D = complex(vector_x[1] ** 2 - 4 * vector_x[2] * vector_x[0]) ** (1/2)

    if(abs(-vector_x[1] + D) < abs(-vector_x[1] - D)):

        x0 = x1
        x1 = x2
        x2 = (-2) * vector_x[0] / (vector_x[1] - D)

    else:

        x0 = x1
        x1 = x2
        x2 = (-2) * vector_x[0] / (vector_x[1] + D)

    counter = counter + 1

    print(counter + 2, x2, f(x2))

else:

    print("failed")