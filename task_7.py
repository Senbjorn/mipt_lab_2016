#task_7
n = int(input())
A = list(map(int, input().split()))
t = int(input())
for i in range(t):
	jump = A[-1]
	for j in range(jump):
		A[-1 - j], A[-2 - j] = A[-2 - j], A[-1 - j]
print(*A)