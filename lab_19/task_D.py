#task_D

def get_neighbour(index, x, y):
	if index == 0:
		return (x, y + 1)
	if index == 1:
		return (x + 1, y)
	if index == 2:
		return (x, y - 1)
	if index == 3:
		return (x - 1, y)

def check(x, y):
	global n, m
	return x >= 0 and y >= 0 and x < m and y < n


n, m = tuple(map(int, input().split()))
a2, a1 = tuple(map(int, input().split()))
b2, b1 = tuple(map(int, input().split()))
graph = [[] for i in range(n * m)]
A = [[None for j in range(m)] for i in range(n)]
for i in range(n):
	s = input()
	for j in range(m):
		if s[j] == 'X':
			A[i][j] = -1
k = 0
Q = [(a1, a2)]
A[a2][a1] = 0
while k < len(Q):
	x, y = Q[k]
	k += 1
	for i in range(4):
		x1, y1 = get_neighbour(i, x, y)
		if check(x1, y1) and A[y1][x1] == None:
			A[y1][x1] = A[y][x] + 1
			Q.append((x1, y1))
if A[b2][b1] == None or A[b2][b1] == -1:
	print('INF')
else:
	print(A[b2][b1])