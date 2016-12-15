#task_9
def rotate_point(i, j, n):
	return (j, n - i - 1)

def Rotate(A):
	for i in range(len(A) // 2):
		for j in range(i, n - i - 1):
			a, b = i, j
			temp = A[i][j]
			for k in range(4):
				(a, b) = rotate_point(a, b, len(A))
				p = A[a][b]
				(A[a][b], temp) = (temp, p)

n = int(input())
A = [input().split() for i in range(n)]
Rotate(A)
for i in range(n):
	print(*A[i])
