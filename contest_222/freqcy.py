def get_next():
    get_next.seed = (get_next.seed*513 + 1)%2**18
    if get_next.seed == 0:
        return 0
    else:
        return (get_next.seed**2 + 3*get_next.seed)%999 + 1
get_next.seed = int(input())
A = 1001 * [0]
n = get_next()
while n != 0:
	A[n] += 1
	n = get_next()
max = 0
for i in range(1, 1001):
	if A[i] > max:
		max = A[i]
for i in range(1, 1001):
	if A[i] == max:
		print(i, end = ' ')