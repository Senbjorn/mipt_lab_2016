#task_5
def y1(x):
	return 1 + x * x
def y2(x):
	return -2 - x * x
x, y = tuple(map(float, input().split()))
if y1(x) < y or y2(x) > y:
	print('YES')
else:
	print('NO')