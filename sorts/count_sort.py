from random import randint

def count_sort(A):
	Q = [0] * 10
	for x in A:
		Q[x] += 1
	pos = 0
	for key in range(10):
		for i in range(Q[key]):
			A[pos] = key
			pos += 1

A = [randint(0, 9) for i in range(30)]
print(*A)
count_sort(A)
print(*A)