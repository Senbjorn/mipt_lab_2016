import sys
import os
try:
	out = open("output.txt", 'w')
	print(os.path.getsize(sys.argv[1]), file = out)
	out.close()
	sys.exit(0)
except IndexError:
	print("Usage: stat filename", file = out)
	out.close()
	sys.exit(1)
except FileNotFoundError:
	print("Can't open file", sys.argv[1], file = out)
	out.close()
	sys.exit(2)
