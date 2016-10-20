#task_6
import codecs

def correction(s):
	k = 0
	while k < len(s):
		if not s[k].isalpha():
			s = s[0: k] + s[k + 1:]
			continue
		k += 1
	return s

file = codecs.open('en-ru6.txt', 'r', 'utf-8')
file2 = codecs.open('ru-en.txt', 'w', 'utf-8')
L = file.readlines()
D = dict()
for line in L:
	key, value = tuple(line.split('\t-\t'))
	D[key] = (value.rstrip('\n')).split()
R = dict()
for key in D.keys():
	for i in range(len(D[key])):
		if D[key][i] in R:
			R[D[key][i]].append(key)
		else:
			R[D[key][i]] = [key]
for r in R.items():
	print(r[0], '\t-\t', *r[1], file = file2)

