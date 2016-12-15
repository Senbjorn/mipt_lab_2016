def hanoi(k, a, b, n):
	if (n == 1 and abs(a-b) == 1):
		print(k, a + 1, b + 1)
		return
	if (n == 1 and abs(a - b) == 2):
		c = a + (b - a) // abs(b-1)
		print(k, a + 1, c + 1)
		hanoi(k, c, b, n)
		return
	if (abs(a - b) == 2):	
		hanoi(k - 1, a, b, n - 1)
		hanoi(k, a, 3 - b - a, 1)
		hanoi(k - 1, b, a, n - 1)
		hanoi(k, 3 - b - a, b, 1)
		hanoi(k, a)
	else:
		hanoi
