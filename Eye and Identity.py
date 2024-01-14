# https://www.hackerrank.com/challenges/np-eye-and-identity

import numpy as np

np.set_printoptions(legacy='1.13')

rows, columns = map(int, input().split())

result_array = np.eye(rows, columns)
print(result_array)