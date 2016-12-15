#task_5
def check(sequence):
	n = 0
	for i in range(len(sequence)):
		n += 1 if sequence[i] == '(' else -1
		if n < 0:
			return False
	return n == 0
s = input()
print('YES' if check(s) else 'NO')
