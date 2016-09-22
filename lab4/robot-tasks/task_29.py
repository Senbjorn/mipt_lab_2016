#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
	m = 0
	while not wall_is_on_the_right():
		if cell_is_filled():
			m += 1
		else:
			m = 0
		if m == 3:
			break
		move_right()



if __name__ == '__main__':
    run_tasks()
