#task_3
import string
input_stream = open("LICENSE.txt", 'r')
s = input_stream.read()
p = string.punctuation
print(len(s), p)
for i in range(len(s)):
	if s[i] in p or s[i] == '\n':
		s = s[0: i] + ' ' + s[i + 1:]
print(s)
s = s.lower()
S = s.split()
D = {}
for a in S:
	if a in D:
		D[a] += 1
	else:
		D[a] = 1
max = 0
max_key = ''
for k in D.keys():
	if max < D[k]:
		max = D[k]
		max_key = k
print(max_key, max)