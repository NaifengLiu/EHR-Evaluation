import numpy as np

test = np.loadtxt("v0")[:, 0]

v_rank = np.argsort(test, axis=0)
print v_rank

v_found = 0
count = 0
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in v_rank:
    if i <= 197:
        v_found += 1
    count += 1
    ratio = v_found / float(197)
    if 1 <= int(ratio/0.05) <= 10:
        if result[int(ratio/0.05)-1] == 0:
            result[int(ratio/0.05)-1] = v_found / float(count) * 100
print result