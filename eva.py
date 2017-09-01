import numpy as np
import os

# v = np.zeros([39597, 2])
# t = np.zeros([49801, 2])
#
#
# for files in os.listdir("/network/rit/lab/ceashpc/nl544752"):
#     if files[0] == "v":
#         v += np.loadtxt("/network/rit/lab/ceashpc/nl544752/" + files)
#     if files[0] == "t":
#         t += np.loadtxt("/network/rit/lab/ceashpc/nl544752/" + files)
#
# np.savetxt("v_result", v)
# np.savetxt("t_result", t)

v_result = np.loadtxt("v_result")
t_result = np.loadtxt("t_result")

v_rank = np.argsort(-v_result, axis=0)
v_rank_final = v_rank[:, 0]

t_rank = np.argsort(-t_result, axis=0)
t_rank_final = t_rank[:, 0]

print v_rank_final
