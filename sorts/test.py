A = [10, None]
p = A
while p[1]:
	print(p[0])
	p = p[1]
print(p, p[1])
p[1] = A
print(A)