#task_6
def SwapColumns(A, i, j):
	for t in range(len(A)):
		assert(i >= 0 and j >= 0 and i < len(A[t]) and j < len(A[t]))
		(A[t][i], A[t][j]) = (A[t][j], A[t][i])

(n, m) = tuple(map(int, input().split()))
A = [input().split() for i in range(n)]
(i, j) = tuple(map(int, input().split()))
SwapColumns(A, i, j)
for i in range(n):
	print(*A[i])