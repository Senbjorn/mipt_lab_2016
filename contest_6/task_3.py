#task_3
(n, m) = tuple(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(n)]
r = 0
c = 0
max = A[r][c]
for i in range(n):
	for j in range(m):
		if A[i][j] > max:
			max = A[i][j]
			r = i
			c = j
print(r, c)