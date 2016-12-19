from random import randint

def lcs(A, B):
	n, m = len(A), len(B)
	M = [[0 for i in range(m + 1)] for j in range(n + 1)]
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			if A[i - 1] == B[j - 1]:
				M[i][j] = M[i - 1][j - 1] + 1
			else:
				M[i][j] = max(M[i][j - 1], M[i - 1][j])
	return M[n][m]

n = 15
m = 15
A = [randint(0, 9) for i in range(n)]
B = [randint(0, 9) for i in range(m)]
print(*A)
print(*B)
print(lcs(A, B))