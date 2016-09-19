x = int(input())
p = int(input())
y = int(input())
i = 0
while x < y:
	i += 1
	x = int((x + p / 100 * x) * 100) / 100
print(i)