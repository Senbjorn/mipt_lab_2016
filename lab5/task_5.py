#task_5
B = input().split()
k = int(B[0])
n = int(B[1])
A = [1 for i in range(k)]
for i in range(k, n + 1):
	A.append(sum(A[i - k: i + 1]))
print(A[n])