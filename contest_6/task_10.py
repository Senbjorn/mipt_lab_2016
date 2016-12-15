#task_10
def isInBounds(A, i, j):
	n = len(A)
	m = len(A[0])
	if i >= 0 and j >= 0 and i < n and j < m:
		if A[i][j] != '*':
			return True
	return False

def fill(A, i, j):
	A[i][j] = '*'
	for n in range(i - 1, i + 2):
		for m in range(j - 1, j + 2):
			if isInBounds(A, n, m):
				A[n][m] += 1

(n, m, k) = tuple(map(int, input().split()))
A = [[0 for j in range(m)] for i in range(n)]
for t in range(k):
	(i, j) = tuple(map(int, input().split()))
	fill(A, i - 1, j - 1)
for i in range(n):
	print(*A[i])
