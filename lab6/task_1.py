#task_1.py
import matplotlib.pyplot as p
import random as r
r.seed(0)
N = [100, 1000, 10000, 100000]
#subplot
for j in range(4):
	p.subplot(2, 2, j + 1)
	val = [r.normalvariate(0, 1) for i in range(N[j])]
	p.hist(val, bins = 100)
p.show()