import numpy as np

test = np.array([[4, 2], [2, 1], [3, 0]])

a = np.argsort(-test, axis=0)

print a[:, 0]
