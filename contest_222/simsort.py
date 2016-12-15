def simsort(A, B):
	n = len(A)
	for i in range(0, n - 1):
		for j in range(1, n):
			if A[j - 1] >= A[j]:
				A[j - 1], A[j] = A[j], A[j - 1]
				B[j - 1], B[j] = B[j], B[j - 1]



A = list(map(int, input().split()))
B = list(map(int, input().split()))
simsort(A, B)
print(*B)
