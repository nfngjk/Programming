import numpy as np

m = eval(input())
n = eval(input())
tolerance = eval(input())

A = np.array([[7, 5, 7, 7], [-2, -5, -6, -7], [-8, 5, -1, 0], [6, -2, -7, 5], [-8, -8, 8, -8], [3, -5, -3, -9]], dtype = float)

original_matrix = A.copy()

print("A = \n", np.round(original_matrix, 3))

E = [i for i in range(0, m)]        # matrix representation of P
F = [i for i in range(0, n)]        # matrix representation of Q

rank = 0

for j in range(0, n):

    pivot_position = np.argmax(abs(A[rank : , j : ]))
    print(pivot_position)
    pivot_row = rank + pivot_position // (n - j)
    pivot_column = j + pivot_position % (n - j)
    pivot = A[pivot_row][pivot_column]

    if(abs(pivot) < tolerance):

        break
    
    if(pivot_row > rank):       # swap rows

        A[[rank, pivot_row]] = A[[pivot_row, rank]]

        E[rank] = pivot_row

    if(pivot_column > j):       # swap column

        A[ : , [j, pivot_column]] = A[ : , [pivot_column, j]]

        F[rank] = pivot_column

    for i in range(rank + 1, m):        # elimination

        scalar = A[i][j] / A[rank][j]

        A[i][j + 1 : ] = A[i][j + 1 : ] - A[rank][j + 1 : ] * scalar

        A[i][rank] = scalar

        print(np.round(A, 3))

    rank = rank + 1

    if(rank >= min(m, n)):

        print(np.round(A, 3))

        break

P = np.identity(m)
Q = np.identity(n)
L = np.identity(m)
U = np.zeros((m, n), dtype = float)

for i in range(0, len(E)):

    P[[i, E[i]]] = P[[E[i], i]]

print("P = \n", np.round(P, 3))

for i in range(0, len(F)):

    Q[[i, F[i]]] = Q[[F[i], i]]

print("Q = \n", np.round(Q, 3))

for j in range(0, rank):

    for i in range(j + 1, rank):

        L[i][j] = A[i][j]

        A[i][j] = 0

print("L = \n", np.round(L, 3))

for i in range(0, m):

    for j in range(i, n):

        U[i][j] = A[i][j]

print("U = \n", np.round(U, 3))

P_dot_A_dot_Q = np.copy(original_matrix)

for i in range(0, len(E)):

    P_dot_A_dot_Q[[i, E[i]]] = P_dot_A_dot_Q[[E[i], i]]

for i in range(0, len(F)):

    P_dot_A_dot_Q[ : ][[i, F[i]]] = P_dot_A_dot_Q[ : ][[F[i], i]]

print(np.linalg.norm(P_dot_A_dot_Q - np.dot(L, U)))