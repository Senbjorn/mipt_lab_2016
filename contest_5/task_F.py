#task_F
n = int(input())
s = input()
A = list(map(int, s.split()))
m = abs(A[0] - A[1])
x1 = 0
x2 = 1
for i in range(len(A)):
	for j in range(i + 1, len(A)):
		if m > abs(A[i] - A[j]):
			m = abs(A[i] - A[j])
			x1 = i
			x2 = j
print(x1, x2)

