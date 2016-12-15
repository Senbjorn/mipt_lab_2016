#task_7
s = input()
c = s.find('.')
s = s[0:c]
A = [0] * 256
ans = str()
for i in range(len(s)):
	A[ord(s[i])] += 1
for i in range(256):
	ans += chr(i) * A[i]
ans += '.'
print(ans)