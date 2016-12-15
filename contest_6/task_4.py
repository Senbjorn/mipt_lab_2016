#task_4
n = int(input())
A = [['.' for i in range(n)] for i in range(n)]
for i in range(n):
	for j in range(n):
		if i == j or n - i - 1 == j or i == n // 2 or j == n // 2:
			A[i][j] = '*'
for i in range(n):
	print(*A[i])