import numpy as np
import re
import math


def relative_error(true_value, errored_value):
    return np.abs((true_value - errored_value) / true_value)


def matching_digits(true_value, errored_value):
    absolute_error = np.abs(true_value - errored_value)
    count_digits = 0
    i = 0
    while i < 30:
        if absolute_error < 10 ** (-i):
            count_digits += 1
            i += 1
        else:
            return count_digits


def error_matrix(matrix, position):
    matrix_neg, matrix_pos = matrix.copy(), matrix.copy()
    matrix_neg[position, position] -= 0.01
    matrix_pos[position, position] += 0.01
    return matrix_neg, matrix_pos


A = np.array([[3, 1, 13],
              [5, 3, 15],
              [11, 5, 40]], dtype=float)
true_det = round(np.linalg.det(A))


print(f"det(A) = {true_det}")
for i in range(3):
    A_neg, A_pos = error_matrix(A, i)
    neg_det = np.linalg.det(A_neg)
    pos_det = np.linalg.det(A_pos)
    print("--------------------------------------------------------------------")
    print(f"det(A with negative error of 1% at {i+1}-{i+1} position) = {neg_det} \n"
          f"relative error: {relative_error(true_det, neg_det)} \n"
          f"amount of correct digits: {matching_digits(true_det, neg_det)}")
    print(f"det(A with positive error of 1% at {i+1}-{i+1} position) = {pos_det} \n"
          f"relative error: {relative_error(true_det, pos_det)} \n"
          f"amount of correct digits: {matching_digits(true_det, pos_det)}")
