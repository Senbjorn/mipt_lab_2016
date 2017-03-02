alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def analysis(text):
	statistics = {key: value for key, value in zip(alphabet, [0.0] * 33)}
	text.lower()
	count = 0.0
	for char in text:
		if char in alphabet:
			count += 1
			statistics[char] += 1
	for key in statistics:
		statistics[key] = statistics[key] * 100 / count
	return statistics

file1 = open("text_1.txt", 'r')
file2 = open("text_2.txt", 'r')
text1 = file1.read()
text2 = file2.read()
s1 = analysis(text1)
s2 = analysis(text2)
a1 = sorted(s1.items(), key = lambda x: x[1])
a2 = sorted(s2.items(), key = lambda x: x[1])
a3 = [(a2[i][0], a1[i][0]) for i in range(len(a1))]
a3 = sorted(a3, key = lambda x: x[1])
for i in range(33):
	print(a1[i], a2[i])
for i in range(33):
	print(a3[i][0], end = '')
