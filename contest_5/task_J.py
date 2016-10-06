#task_J
n = int(input())
A = list(map(int, input().split()))
t = 0
r = 0
for i in range(len(A)):
	if A[i] == 5:
		t += 1
	else:
		k = A[i] // 5 - 1
		if (k >= t):
			r += k - t
			t = 0
		else:
			t -= k
print(r)
