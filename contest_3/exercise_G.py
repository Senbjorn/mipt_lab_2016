i = 0
c = 0
b = 0
a = int(input())
while a != 0:
	c += a * a
	b += a
	i += 1
	a = int(input())
print(((c / i - (b / i) ** 2) * i / (i - 1)) ** (1 / 2))