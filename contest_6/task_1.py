#task_1
def solve(a, b, c, d):
	a = min(a, b)
	c = min(c, d)
	return min(c, a)

(a, b, c, d) = tuple(map(int, [int(input()) for i in range(4)]))
print(solve(a, b, c, d))