#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
	n = 0
	m = 0
	move_right()
	while not wall_is_on_the_right():
		if m == n :
			fill_cell()
			n += 1
			m = 0
		move_right()
		m += 1


if __name__ == '__main__':
    run_tasks()
