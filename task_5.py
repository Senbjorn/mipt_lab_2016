#task_5
n, m = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = [A[i * m: (i + 1) * m] for i in range(n)]
for i in range(n):
	print(*B[i])