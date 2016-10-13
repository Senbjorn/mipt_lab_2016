#task_4
n = 3
B = input().split()
A = [B[3 * i: 3 * (i + 1)] for i in range(n)]
A[0], A[2] = A[2], A[0]
for i in range(n):
	print(*A[i])