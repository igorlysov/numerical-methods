import numpy as np
from itertools import product

A = np.array([[3, 1, 13],
              [13.4, 11.4, 23],
              [5, 3, 15]], dtype=np.float64)
alpha = 0.1
beta = 0.2
true_det = round(np.linalg.det(A), 2)
# equals 1.6 so that inverse matrix exists for A
n, m = 3, 3
x = product([1, -1], repeat=n*m)
x = np.reshape(list(x), (-1, n, m))

print((3 ** 25) * (4 ** 2))
