from random import randint

def merge(L, R):
	i, j = 0, 0
	M = [None] * (len(L) + len(R))
	while i < len(L) and j < len(R):
		if L[i] > R[j]:
			M[i + j] = R[j]
			j += 1
		else:
			M[i + j] = L[i]
			i += 1
	return M[:i + j] + L[i:] + R[j:]

def merge_sort(A):
	if len(A) <= 1:
		return A
	L = merge_sort(A[:len(A) // 2])
	R = merge_sort(A[len(A) // 2:])
	return merge(L, R)

a = Point(2, 3)
A = [randint(0, 500) for i in range(10)]
print(*A)
B = merge_sort(A)
print(*B)