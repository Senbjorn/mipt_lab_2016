#task_2
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

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*merge(A, B))