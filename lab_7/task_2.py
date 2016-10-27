#task_2
import sys
import argparse

parser = argparse.ArgumentParser(description = 'Calculator')
parser.add_argument(
	'values',
	metavar = 'VALUES',
	type = float,
	nargs = '+',
	help = 'numbers we are to use'
)
parser.add_argument(
	'-v',
	'--verbose',
	action = 'store_true',
	help = 'show the expression'
)
parser.add_argument(
	'-a',
	'--action',
	metavar = 'ACTION',
	type = str,
	action = 'store'
)

args = parser.parse_args()
operators = ['+', '-', '*', '/']
# print(args.action in operators)
if not (args.action in operators):
	print(
		'You have to use option --action with one of following valuse: +, -, *, /',
		file=sys.stderr
	)
	sys.exit(-1)
if len(args.values) != 2:
	print(
		'only two values in VAlUES are acceptable',
		file = sys.stderr
	)
	sys.exit(-1)
values = args.values
if args.verbose:
	print(values[0], args.action, values[1])
print(eval(str(values[0]) + args.action + str(values[1])))