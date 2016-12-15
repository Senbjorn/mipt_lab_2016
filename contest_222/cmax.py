def get_next():
    get_next.seed = (get_next.seed*513 + 1)%2**18
    return 0 if get_next.seed == 0 else (get_next.seed**2%100000 + 1)
get_next.seed = int(input())
n = get_next()
cmax = 0
t = 0
A = list()
while n != 0:
	if n > cmax:
		cmax = n
		A = list()
		A.append(t)
	elif n == cmax:
		A.append(t)
	n = get_next()
	t += 1
print(*A)