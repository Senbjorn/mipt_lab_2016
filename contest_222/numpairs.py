k = 0
a, b = tuple(map(int, input().split()))
while a != 0 or b != 0:
	if (a % 9 == 0 and b % 9 == 0) or (a % 3 == 0 and b % 2 == 0 and b % 3 != 0) or (b % 3 == 0 and a % 2 == 0 and a % 3 != 0):
		k += 1
	a, b = tuple(map(int, input().split()))
print(k)