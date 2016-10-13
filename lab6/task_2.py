#task_2.py
import random as r
def function(x):
	assert(-3 <= x and 3 >= x)
	if x <= 2 and x >= -2:
		return -x ** 2 + 4
	else:
		return 0


n = 1000
a = -3
b = 3
print(B)
val = [function(r.uniform(a, b)) for i in range(n)]
answer = (b - a) / n * sum(val)
print(answer)