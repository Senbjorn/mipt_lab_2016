#task_3
n = int(input())
F = [0] * n
G = [0] * n
for i in range(2, n):
	F[i] = F[i - 1] + 2 * G[i - 2] + 1
	G[i] = F[i - 2] + 2 * G[i - 1] - 1
print(F[n - 1])