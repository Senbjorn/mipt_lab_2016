#task_3
def count(first = True):
	s = 1 if first else 0
	temp = first
	for i in range(len(answers) - 1):
		s += 1 if temp ^ answers[i] == 0 else 0
		temp = temp ^ answers[i] == 0
	return s
n = int(input())
answers = list(map(int, input().split()))
print(min(count(first = True), count(first = False)))
