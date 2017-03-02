#task_F
def jump(A):
	n = len(A)
	Q = [0]
	D = [fund, 0] + [None] * (n - 2)
	index = 0
	while index < len(Q):
		x = Q[index]
		index += 1
		if (x + 2 < n and (D[x + 2] == None or (100 + A[x + 2]) / 100 * 
			D[x] > D[x + 2])):
			D[x + 2] = (100 + A[x + 2]) / 100 * D[x]
			Q.append(x + 2)
		if (x + 3 < n and (D[x + 3] == None or (100 + A[x + 3]) / 100 * 
			D[x] > D[x + 3])):
			D[x + 3] = (100 + A[x + 3]) / 100 * D[x]
			Q.append(x + 3)
	return D

def get_path(D):
	x = D.index(max(D))
	P = [x + 1]
	while x != 0:
		if x - 3 >= 0 and D[x -2] * (100 + A[x]) / 100 < D[x -3] * (100 + A[x]) / 100:
			P.append(x - 2)
			x -= 3
		else:
			P.append(x - 1)
			x -= 2
	return P[-1::-1]

fund = int(input())
A = list(map(int, input().split()))
D = jump(A)
print(*get_path(D))


