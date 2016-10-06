#task_9
n = int(input())
A = list(map(int, input().split()))
k = int(input())
max = 0
for i in range(n - k + 1):
	if max < sum(A[i:k + i]):
		max = sum(A[i:k + i])
print(max)