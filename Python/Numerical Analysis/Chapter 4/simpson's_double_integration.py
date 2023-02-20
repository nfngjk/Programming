import numpy as np
from sympy import *

a = eval(input())
b = eval(input())
m = eval(input())
n = eval(input())

x = Symbol("x")
y = Symbol("y")
f = exp(y / x)
f = lambdify([x, y], f)

delta_x = (b - a) / 2

end_term_x = 0
even_term_x = 0
odd_term_x = 0

approximation = 0

for i in range(0,n + 1):

    f1 = x ** 3
    f2 = x ** 2

    delta_y =  (f2 - f1) / m

    even_term_y = 0
    odd_term_y = 0

    for j in range(1, m):
        
        if(j % 2 == 0):

            even_term_y = even_term_y + f(x, f1 + j * delta_y)

        else:

            odd_term_y = odd_term_y + f(x, f1 + j * delta_y)

    limit_of_first_integral = (delta_y / 3) * (f(x, f1) + 4 * odd_term_y + 2 * even_term_y + f(x, f2))

    if(i == 0 or i == n):
 
        end_term_x = end_term_x + limit_of_first_integral

    elif(i % 2 == 0):

        even_term_x = even_term_x + limit_of_first_integral

    else:

        odd_term_x = odd_term_x + limit_of_first_integral

approximation = (delta_x / 3) * (end_term_x + 4 * odd_term_x + 2 * even_term_x)

print(approximation)