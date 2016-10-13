#task_9
def Capitalize(S):
	for i in range(len(S)):
		if i == 0:
			if S[i].isalpha():
				S =S[0: i] + S[i].upper() + S[i + 1: len(S)]
		else:
			if not S[i - 1].isalpha() and S[i].isalpha():
				S = S[0: i] + S[i].upper() + S[i + 1: len(S)]
			elif S[i - 1].isalpha() and S[i].isalpha():
				S = S[0: i] + S[i].lower() + S[i + 1: len(S)]
	return S

s = input()
print(Capitalize(s))