import numpy as np

m = eval(input())
n = eval(input())
tolerance = eval(input())

matrix = np.array(np.random.randint(-10, 10, (m, n)), dtype = float)
A = np.copy(matrix)

def sgn(x):

    if(x < 0):

        return -1

    else:

        return 1

rank = 0

Q = np.identity(m)

for j in range(0, n):

    x = np.copy(A[rank : ][j])

    xTx = np.dot(x, x)

    if(xTx < tolerance):

        continue

    y = np.zeros(m - rank)

    y[0] = -sgn(x[0]) * np.sqrt(xTx)

    A[rank : , j] = y

    v = x - y

    vTv = 2 * (xTx + abs(x[0])) * np.sqrt(xTx)

    for k in range(j + 1, n):

        z = A[rank : ][k]

        temp = 2 * np.dot(v, z) / vTv

        A[rank : ][j] = z - temp * v

    u = np.reshape(v, (m - rank, 1))

    H = np.identity(m - rank) - 2 / vTv * np.dot(u, u.T)
    Hv = np.identity(m)
    Hv[rank : ][rank : ] = H

    Q = np.dot(Q, Hv)

    rank = rank + 1

print(A)
print(np.round(np.dot(Q, matrix), 2))