b = 0
m, k = int(input()), int(input())
b += m
while m != 0 or k != 0:
	m, k = k, int(input())
	b += m
print(b)
