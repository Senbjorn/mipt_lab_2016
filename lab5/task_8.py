#task_8
n = int(input())
A = list()
for i in range(n):
	A.append(list(map(int, input().split())))
t = int(input())
p = 0
for i in range(len(A)):
	if (A[i][0] <= t and A[i][1] >= t):
		p += 1
print(p)