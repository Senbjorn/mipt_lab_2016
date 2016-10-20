#task_4
import codecs

def correction(s):
	k = 0
	while k < len(s):
		if not s[k].isalpha():
			s = s[0: k] + s[k + 1:]
			continue
		k += 1
	return s

def trnaslate(s, D):
	A = s.split()
	for i in range(len(A)):
		if not A[i][-1].isalpha():
			s1 = A[i][0:-1]
			print(s)
			if A[i][0:-1] in D:
				A[i] = D[A[i][0:-1]] + A[-1]
		elif A[i] in D:
			A[i] = D[A[i]]
	return ' '.join(A)


input_stream = codecs.open('en-ru4.txt', 'r', 'utf-8')
input_stream2 = codecs.open('input4.txt', 'r', 'utf-8')
output_stream = open('translation4.txt', 'w')
D = dict()
L = input_stream.readlines()
for line in L:
	key, value = tuple(line.split('\t-\t'))
	D[correction(key)] = correction(value)
S = input_stream2.read()
print(trnaslate(S.lower(), D), file = output_stream)
input_stream.close()
input_stream2.close()
output_stream.close()