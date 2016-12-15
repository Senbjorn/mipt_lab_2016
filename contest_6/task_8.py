#task_8
def Transpose(A):
	n = len(A)
	m = len(A[0])
	return [[A[j][i] for j in range(n)] for i in range(m)]

(n, m) = tuple(map(int, input().split()))
A = [input().split() for i in range(n)]
B = Transpose(A)
for i in range(len(B)):
	print(*B[i])