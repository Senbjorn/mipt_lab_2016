import sys
s = 0
for item in sys.argv[1:]:
	try:
		s += int(item)
	except ValueError:
		continue
sys.exit(s)