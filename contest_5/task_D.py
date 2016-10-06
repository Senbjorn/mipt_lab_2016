#task_D
def isIP(s):
	if s.count('.') != 3:
		return False
	A = s.split('.')
	if len(A) != 4:
		return False
	for i in range(4):
		if not A[i].isdigit():
			return False
		if A[i][0] == '0' and len(A[i]) != 1:
			return False
		if int(A[i]) > 255:
			return False
	return True

s = input()
if isIP(s):
	print('YES')
else:
	print('NO')
