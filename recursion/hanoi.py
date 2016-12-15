def hanoi(n, i, k):
	if n == 1:
		print('переложить с', i, 'на', k)
	else:
		tmp = 6 - i - k
		hanoi(n - 1, i, tmp)
		print('переложить', n, 'блин с', i, 'на', k)
		hanoi(n - 1, tmp, k)

hanoi(4, 1, 3)