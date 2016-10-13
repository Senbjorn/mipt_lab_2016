#task_8
def euclid_alg(a, b):
	assert(a >= 0 and b >= 0)
	if a > b:
			a, b = b, a
	if a == 0:
		return b
	else:
		return euclid_alg(a, b % a)


n = int(input())
for i in range(n):
	(a, b) = tuple(map(int, input().split()))
	if euclid_alg(a, b) == 1:
		print(a, b)