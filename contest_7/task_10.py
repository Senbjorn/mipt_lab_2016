#task_10
def compare(a, b):
	if len(a) > len(b):
		return 1
	if len(a) < len(b):
		return -1
	sa = a[-1:: -1]
	sb = b[-1:: -1]
	for i in range(len(sa)):
		if ord(sa[i]) > ord(sb[i]):
			return 1
		if ord(sa[i]) < ord(sb[i]):
			return -1
	return 0


def bubble_sort(list):
	for i in range(len(list)):
		for j in range(0, len(list) - 1 - i):
			if compare(list[j], list[j + 1]) == 1:
				list[j], list[j + 1] = list[j + 1], list[j]

n = int(input())
list = [input() for i in range(n)]
bubble_sort(list)
k = 0
for e in list:
	if len(e) != k:
		k = len(e)
		print(k)
	print(e[-1:: -1], e)
	