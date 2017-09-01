import numpy as np
import os

v = np.zeros([39597, 2])
t = np.zeros([49801, 2])


for files in os.listdir("/network/rit/lab/ceashpc/nl544752"):
    if files[0] == "v":
        v += np.loadtxt("/network/rit/lab/ceashpc/nl544752/" + files)
    if files[0] == "t":
        t += np.loadtxt("/network/rit/lab/ceashpc/nl544752/" + files)

np.savetxt("v_result", v)
np.savetxt("t_result", t)
