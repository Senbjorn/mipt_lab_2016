import sys

for f in sys.stdin:
	if f.find(sys.argv[1])!=-1:
		print(f,end='')