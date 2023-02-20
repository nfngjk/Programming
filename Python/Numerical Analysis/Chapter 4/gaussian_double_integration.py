import numpy as np
from sympy import *

m = eval(input())
n = eval(input())

x = Symbol("x")
y = Symbol("y")

# rodrigue's formula
P_n1 = diff(pow(x ** 2 - 1, n), x, m)
P_n2 = diff(pow(x ** 2 - 1, n), x, n)

legendre_polynomial_1 = Poly(P_n1).all_coeffs()
legendre_polynomial_2 = Poly(P_n2).all_coeffs()

# the roots of legendra polynomial
roots_1 = np.roots(legendre_polynomial_1)
roots_2 = np.roots(legendre_polynomial_2)

lagrange_polynomial_1 = 0
lagrange_polynomial_2 = 0

coefficient_1 = np.zeros(m)
coefficient_2 = np.zeros(n)

for i in range(0, m):

    lagrange_intepolation_1 = 1

    for j in range(0, m):

        if(j != i):

            lagrange_intepolation_1 = lagrange_intepolation_1 * (x - roots_1[j]) / (roots_1[i] - roots_1[j])

    coefficient_1[i] = integrate(lagrange_intepolation_1, (x, -1, 1))

for i in range(0, n):

    lagrange_intepolation_2 = 1

    for j in range(0, n):

        if(j != i):

            lagrange_intepolation_2 = lagrange_intepolation_2 * (x - roots_2[j]) / (roots_2[i] - roots_2[j])

    coefficient_2[i] = integrate(lagrange_intepolation_2, (x, -1, 1))

a = eval(input())
b = eval(input())

c = x ** 3
d = x ** 2
f = exp(y / x)

c = lambdify(x, c)
d = lambdify(x, d)
f = lambdify([x, y], f)

midpoint_1 = (b + a) / 2
delta_1 = (b - a) / 2

summation_1 = 0

for i in range(0, m):

    X = delta_1 * roots_1 + midpoint_1

    midpoint_2 = (d(X) + c(X)) / 2
    delta_2 = (d(X) - c(X)) / 2

    summation_2 = 0

    for j in range(0, n):

        Y = delta_2[i] * roots_2 + midpoint_2[i]

        summation_2 = summation_2 + coefficient_2[j] * f(X[i], Y[j])

    summation_1 = summation_1 + coefficient_1[i] * delta_2[i] * summation_2

summation_1 = summation_1 * delta_1

print(summation_1)