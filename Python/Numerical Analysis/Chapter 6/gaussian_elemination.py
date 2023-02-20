import numpy as np

np.random.seed(123)

m = eval(input())
n = eval(input())
tolerance = eval(input())

A = np.array(np.random.randint(-10, 10, (m, n)), dtype = float)

rank = 0

for j in range(0, n):

    pivot_position = np.argmax(abs(A[rank : ][j]))      # find the max argument position

    pivot = A[pivot_position][j]