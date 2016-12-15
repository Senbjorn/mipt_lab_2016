#task_4
import sys
import argparse
import os

def check_path(path, f, i, e, a):
	if os.path.isfile(path) and f:
		return False
	if i != None and os.path.isfile(path) and not i in os.path.basename(path):
		return False
	if e != None and os.path.isfile(path) and e in os.path.basename(path):
		return False
	if not a and (os.path.basename(path))[0] == '.':
		return False
	return True

def fromat_print(path, n, offset, last = False):
	s0 = ''
	for i in range(offset):
		if i != offset - 1:
			s0 += '│    '
		elif last:
			s0 += '├─── '
	if n:
		print(s0, path, sep = '')
	else:
		print(s0, os.path.basename(path), sep = '')

def print_tree(offset, path, f, i, e, a, n):
	dir_list = os.listdir(path)
	for k in range(len(dir_list)):
		path_1 = os.path.join(path, dir_list[k])
		if not check_path(path_1, f, i, e, a):
			continue
		if os.path.isfile(path_1):
			fromat_print(path_1, n, offset)
		elif os.path.isdir(path_1):
			fromat_print(path_1, n, offset)
			print_tree(offset + 1, path_1, f, i, e, a, n)

parser = argparse.ArgumentParser(
	description = 'Parameters of tree'
)
parser.add_argument(
	'-f',
	'--folders-only',
	action = 'store_true',
	help = 'Не отображать файлы в дереве'
)
parser.add_argument(
	'-i',
	'--include',
	metavar = 'SOME_TEXT',
	action = 'store',
	type = str,
	help = 'Отображать только те файлы, в названии которых встречается текст SOME_TEXT'
)
parser.add_argument(
	'-e',
	'--exclude',
	metavar = 'SOME_TEXT',
	action = 'store',
	type = str,
	help = 'Не отображать те файлы, в названии которых встречается текст SOME_TEXT'
)
parser.add_argument(
	'-a',
	'--all',
	action = 'store_true',
	help = 'Отображать скрытые файлы/директории'
)
parser.add_argument(
	'-n',
	'--full-name',
	action = 'store_true',
	help = 'выводить полный текущий путь'
)
parser.add_argument(
	'dir',
	metavar = 'DIR',
	type = str,
	nargs = '?',
	help = 'Каталог'
)

args = parser.parse_args()
if not os.path.exists(args.dir) or not os.path.isdir(args.dir):
	print(
		'Указанный путь не существует или не является папкой',
		file = sys.stderr
	)
	sys.exit(-1)
print_tree(1,
	args.dir,
	args.folders_only,
	args.include,
	args.exclude,
	args.all,
	args.full_name
)
os.system('')
# print("\033[91mКрасный \033[0m ...")