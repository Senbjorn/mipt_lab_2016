#task_10
A = [0, 1, 0]
n = int(input())
for i in range(1, n + 1):
	B = [0]
	for j in range(1, i + 1):
			B.append(A[j - 1] + A[j])
	B.append(0)
	print(*B[1:len(B) - 1])
	A = list(B)