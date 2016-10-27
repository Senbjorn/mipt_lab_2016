#task_1
import sys
n = 0
for i in range(1, len(sys.argv)):
	if (len(sys.argv[i]) % 3 == 0):
		n += 1
print(n)