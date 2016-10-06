#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_4():
	m = 0
	while not wall_is_on_the_right():
		m += fill()
		if not wall_is_on_the_right():
			move_right()
		else:
			break
	mov('ax', m)

def fill():
	n = 0
	if wall_is_above():
		fill_cell()
	else:
		while not wall_is_above():
			move_up()
			if not cell_is_filled():
				fill_cell()
			else:
				n += 1
		while not wall_is_beneath():
			move_down()
	return n



if __name__ == '__main__':
    run_tasks()
