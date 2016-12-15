#task_8
def compare(a, b):
	while a > 0 or b > 0:
		na = a % 10
		nb = b % 10
		a //= 10
		b //= 10
		if na < nb:
			return -1
		if na > nb:
			return 1
	return 0

def bubble_sort(list):
	for i in range(len(list)):
		for j in range(0, len(list) - 1 - i):
			if compare(list[j], list[j + 1]) == 1:
				list[j], list[j + 1] = list[j + 1], list[j]

n = int(input())
list = list(map(int, input().split()))
bubble_sort(list)
print(*list)