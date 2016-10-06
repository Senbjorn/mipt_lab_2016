#task_3
input = open('in_3.txt', 'r')
output = open('out_3.txt', 'w')
A = input.readline().split()
for i in range(len(A)):
	if i % 2 == 0:
		print(A[i // 2], file = output, end = ' ')
	else:
		print(A[len(A) - (i + 1) // 2], file = output , end = ' ')
input.close()
output.close()