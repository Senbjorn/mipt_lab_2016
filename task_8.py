#task_8
n = 8
m = 8
def firstID(x, y):
	global m
	return m - 1 - x + y

def secondID(x, y):
	global n, m
	return m - 1 + n - 1 - x - y

FD = [False for i in range(m + n - 1)]
SD = [False for i in range(m + n - 1)]
R = [False for i in range(m)]
C = [False for i in range(n)]
A = False
for i in range(8):
	x, y = tuple(map(lambda a: int(a) - 1, input().split()))
	if R[x] or C[y] or FD[firstID(x, y)] or SD[secondID(x, y)]:
		A = True
	else:
		R[x] = True
		C[y] = True
		FD[firstID(x, y)] = True
		SD[secondID(x, y)] = True
if A:
	print("YES")
else:
	print("NO")