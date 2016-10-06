#task_E
s = '1'
n = int(input())
for i in range(n - 1):
	s1 = ''
	c = s[0]
	k = 1
	for j in range(1 ,len(s) + 1):
		if j != len(s):
			if c == s[j]:
				k += 1
			if c != s[j]:
				s1 = s1 + str(k) + c
				c = s[j]
				k = 1
		else:
			s1 = s1 + str(k) + c
	s = s1
print(s)
