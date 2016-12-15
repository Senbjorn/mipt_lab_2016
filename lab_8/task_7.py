#task_7
import codecs

def updateDict(A, B):
	for key in B.keys():
		Wb = B[key]
		for word in Wb:
			if word in A:
				Wa = A[word]
				if not key in Wa:
					Wa.append(key)
			else:
				A[word] = [key]

en = codecs.open('en-ru7.txt', 'r', 'utf-8')
ru = codecs.open('ru-en7.txt', 'r', 'utf-8')
uen = codecs.open('Uen-ru7.txt', 'w', 'utf-8')
uru = codecs.open('Uru-en7.txt', 'w', 'utf-8')
L = en.readlines()
EN = dict()
for line in L:
	key, value = tuple(line.split('\t-\t'))
	EN[key] = (value.rstrip('\n')).split(',')
L = ru.readlines()
RU = dict()
for line in L:
	key, value = tuple(line.split('\t-\t'))
	RU[key] = (value.rstrip('\n')).split(',')
updateDict(RU, EN)
updateDict(EN, RU)
for r in RU.items():
	print(r[0], '\t-\t', ', '.join(r[1][0:]), file = uru)
print()
for e in EN.items():
	print(e[0], '\t-\t', ', '.join(e[1][0:]), file = uen)
en.close()
ru.close()
Uen.close()
Uru.close()