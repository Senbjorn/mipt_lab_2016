def compare(c1, c2):
	global dost, masti
	if dost[c1[0]] > dost[c2[0]]:
		return 1
	elif dost[c1[0]] < dost[c2[0]]:
		return -1
	else:
		if masti[c1[1]] > masti[c2[1]]:
			return 1
		elif masti[c1[1]] < masti[c2[1]]:
			return -1
		else:
			return 0

dost = {
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'T': 10,
	'J': 11,
	'Q': 12,
	'K': 13,
	'A': 14, 
}
masti = {
	'c': 1,
	's': 2,
	'h': 3,
	'd': 4,
}
n = int(input())
A = input()
A = [A[i * 2: i * 2 + 2] for i in range(n)]
for i in range(1, n):
	val = A[i]
	j = i - 1
	while (j >= 0) and compare(A[j], val) == 1:
		A[j + 1] = A[j]
		j = j - 1
	A[j + 1] = val
print(*A, sep = '')