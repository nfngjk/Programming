import numpy as np

m = eval(input())
n = eval(input())
tolerance = eval(input())

A = np.array([[7, 5, 7, 7], [-2, -5, -6, -7], [-8, 5, -1, 0], [6, -2, -7, 5], [-8, -8, 8, -8], [3, -5, -3, -9]], dtype = float)

original_matrix = A.copy()      # original matrix

E = [i for i in range(0, min(m, n))]        # matrix representation
F = [i for i in range(0, min(m, n))]        # matrix representation

rank = 0

for j in range(0, n):

    pivot_position = rank + np.argmax(abs(A[rank : , j : ]))       # find the pivot position
    p = rank + (pivot_position - rank) // (n - j)
    q = j + (pivot_position - rank) % (n - j)
    pivot = A[p][j]

    if(abs(pivot) < tolerance):

        break

    if(pivot_position > rank):      #swap rows

        A[[rank, p]] = A[[p, rank]]

        E[rank] = p

    if(q > j):      # swap columns

        A[ : , [j, q]] = A[ : , [q, j]]

        F[rank] = q

    for i in range(rank + 1, m):        # elimination

        scalar = A[i][j] / A[rank][j]

        A[i][j + 1 : ] = A[i][j + 1 : ] - A[rank][j + 1 : ] * scalar
        # A[i][rank] = scalar

        print(np.round(A, 4))

    rank = rank + 1

    if(rank >= min(m, n)):

        print(np.round(A, 4))

        break

P = np.identity(m)
L = np.identity(m)
Q = np.identity(n)

for j in range(0, rank):

    L[j + 1 : , j] = A[j + 1 : , j]

    A[j + 1 : , j] = 0

print(np.round(L, 3))
print(np.round(np.dot(L, A), 3))

for i in range(min(m, n)):

    P[[i, E[i]]] = P[[E[i], i]]

for i in range(0, min(m, n)):

    Q[[i, F[i]]] = Q[[F[i], i]]

print(P)
print(Q)

P_dot_A_dot_Q = np.copy(original_matrix)

for i in range(0, len(E)):

    P_dot_A_dot_Q[[i, E[i]]] = P_dot_A_dot_Q[[E[i], i]]

for i in range(0, len(F)):

    P_dot_A_dot_Q[ : , [i, F[i]]] = P_dot_A_dot_Q[ : , [F[i], i]]

print(np.linalg.norm(P_dot_A_dot_Q - np.dot(L, A)))