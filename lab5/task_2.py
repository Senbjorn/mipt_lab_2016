#task_2
A = input().split()
for i in range(1,len(A),2):
	A[i - 1: i], A[i: i + 1] = A[i: i + 1], A[i - 1: i]
print(' '.join(A))
A = A[len(A) - 1:len(A)]+A[0:len(A) - 1]
print(' '.join(A))
print(' '.join([A[i] for i in range(len(A)) if A.count(A[i]) == 1]))
max = 1
n = 0
for i in range(len(A)):
	if A.count(A[i]) > max:
		max = A.count(A[i])
		n = i
print(A[n])
