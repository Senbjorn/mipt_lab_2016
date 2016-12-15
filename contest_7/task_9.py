#task_9
def compare(a, b):
	return 1 if a[1] > b[1] else -1 if a[1] < b[1] else -1 if a[0] > b[0] else 1 if a[0] < b[0] else 0


def bubble_sort(list):
	for i in range(len(list)):
		for j in range(0, len(list) - 1 - i):
			if compare(list[j], list[j + 1]) == 1:
				list[j], list[j + 1] = list[j + 1], list[j]

n = int(input())
list = [tuple(map(float, input().split())) for i in range(n)]
bubble_sort(list)
for e in list:
	print('%.2f' %e[0], '%.3f' %e[1])