import numpy as np

def Newton_division_difference(x, y):

    n = len(y)

    coefficients = np.zeros((n, n))

    coefficients[:, 0] = y

    for j in range(1, n):

        for i in range(n - 1, j - 1, -1):

            coefficients[i][j] = (coefficients[i][j - 1] - coefficients[i - 1][j - 1]) / (x[i] - x[i - j])

    return coefficients

def polynomial(coefficient, x_i, x):

    n = len(x_i) - 1

    p = coefficient[n]

    for k in range(1, n + 1):

        p = coefficient[n - k] + (x - x_i[n - k]) * p
    
    return p

x = np.array([1.0, 1.3, 1.6, 1.9, 2.2])
y = np.array([0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623])

print(Newton_division_difference(x, y))