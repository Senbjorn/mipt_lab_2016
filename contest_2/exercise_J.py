a, b, i = 0, 1, 1
n = int(input())
while b < n:
	a, b, i = b, a + b, i + 1
if n == b:
	print(i)
else:
	print(-1)