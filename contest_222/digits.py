n = abs(int(input()))
k = 0
b = 17
while n != 0:
	if n % 17 == 16:
		k += 1
	n //= 17	
print(k)