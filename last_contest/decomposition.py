
n = int(input())
A = [[1 if j == 0 else 0 for j in range(n)] for i in range(n)]
for j in range(1, n):
	for i in range(0, n):
		if i == 0  and j == 0:
			continue
		if i >= j:
			A[i][j] = A[j - 1][j] + 1
			continue
		for k in range(i + 1):
			A[i][j] += A[k][j - 1 - k]
print(A[n - 1][n - 1])