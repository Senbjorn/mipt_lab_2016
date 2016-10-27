#task_3
import sys
args = sys.argv
for i in range(1, len(args)):
	stream = open(args[i], 'r')
	print(stream.read())
	stream.close()
