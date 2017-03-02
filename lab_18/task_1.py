n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
B = list()
for i in range(n):
	for j in range(n):
		if A[i][j] != 0:
			B.append([i, j, A[i][j]])
for x in B:
	print(*x)
