#lect 6
from random import randint
def count_deg(a):
	deg = 0
	while a != 0:
		a //= 10
		deg += 1
	return deg

from math import *
def radix_sort(A):
	M = max(A)
	size = count_deg(M)
	for i in range(size):
		r = 10 ** (i + 1)
		Q = [list() for i in range(10)]
		for x in A:
			radix = 10 * (x % r) // r
			Q[radix].append(x)
		pos = 0
		for key in range(10):
			for x in Q[key]:
				A[pos] = x
				pos += 1

A = [randint(1775, 1778) for i in range(10)]
print(*A)
radix_sort(A)
print(*A)




