#task_6
n, m = tuple(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(n)]
B = [[A[n - j - 1][i] for j in range(n)] for i in range(m)]
for i in range(m):
	print(*B[i])
