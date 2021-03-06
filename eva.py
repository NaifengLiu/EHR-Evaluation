import numpy as np
import os

# v = np.zeros([39597, 2])
# t = np.zeros([49801, 2])
#
#
# for files in os.listdir("/network/rit/lab/ceashpc/bz383376/naifeng"):
#     if files[0] == "v":
#         v += np.loadtxt("/network/rit/lab/ceashpc/bz383376/naifeng/" + files)
#     if files[0] == "t":
#         t += np.loadtxt("/network/rit/lab/ceashpc/bz383376/naifeng/" + files)
#
# np.savetxt("v_result", v)
# np.savetxt("t_result", t)

v_result = np.loadtxt("v_result")
t_result = np.loadtxt("t_result")

v_rank = np.argsort(-v_result, axis=0)
v_rank_final = v_rank[:, 0]

t_rank = np.argsort(-t_result, axis=0)
t_rank_final = t_rank[:, 0]

v_found = 0
count = 0
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in v_rank_final:
    if i <= 197:
        v_found += 1
    count += 1
    ratio = v_found / float(197)
    if 1 <= int(ratio/0.05) <= 10:
        if result[int(ratio/0.05)-1] == 0:
            result[int(ratio/0.05)-1] = v_found / float(count) * 100
print result

t_found = 0
count = 0
for i in t_rank_final:
    if i <= 197:
        t_found += 1
    count += 1
    if t_found / float(197) >= 0.05:
        print "t_recall at 0.05: " + str(t_found / float(count) * 100) + "%"
        break
