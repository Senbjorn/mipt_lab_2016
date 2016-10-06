#task_4
A = list(map(int, input().split()))
t = int(input())
for i in range(t):
	A.insert(len(A) - A[len(A) - 1] - 1, A[len(A) - 1])
	A.pop()
print(*A)
