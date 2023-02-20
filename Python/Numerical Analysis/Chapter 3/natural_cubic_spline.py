import numpy as np
import matplotlib.pyplot as plt

x = [4, 5, 6, 7]
y = [3, -2, -4, 1]
number_of_point = len(x)

h = np.zeros(number_of_point - 1)           # the value of the subdiagonal and superdiagonal in matrix A

for i in range(0, number_of_point - 1): 
    
    h[i] = x[i + 1] - x[i]

A = np.zeros((number_of_point, number_of_point))
B = np.zeros(number_of_point)

A[0][0] = 1
A[number_of_point - 1][number_of_point - 1] = 1

B[0] = 0 
B[number_of_point - 1] = 0

for i in range(1, number_of_point - 1):
    
    A[i][i - 1] = h[i - 1] / 6
    A[i][i] = (h[i - 1] + h[i]) / 3
    A[i][i + 1] = h[i] / 6
    
    B[i] = (y[i + 1] - y[i])  / h[i] - (y[i] - y[i - 1]) / h[i - 1] 

vector_x = np.linalg.solve(A, B)            # solve Ax = B

a = np.zeros(number_of_point - 1)
b = np.zeros(number_of_point - 1)
c = np.zeros(number_of_point - 1)

for j in range(0, number_of_point - 1):

    c[j] = (y[j + 1] - y[j]) / h[j] - ((2 * vector_x[j] + vector_x[j + 1]) / 6) * h[j]    
    b[j] = vector_x[j] / 2
    a[j] = ((vector_x[j + 1] - vector_x[j]) / 6) / h[j]

S = lambda j, t: y[j] + (t - x[j]) * (c[j] + (t - x[j]) * (b[j] + (t - x[j] * a[j]))) 


for j in range(0, number_of_point - 1):

    print("[%f, %f, %f, %f]" %(y[j], c[j], b[j], a[j]))