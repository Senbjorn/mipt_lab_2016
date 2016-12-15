#task_5
(n, m) = tuple(map(int, input().split()))
A = [['.' if (i + j) % 2 == 0 else '*' for j in range(m)] for i in range(n)]
for i in range(n):
	print(*A[i])