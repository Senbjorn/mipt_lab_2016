#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
	m = 0
	while True:
		if cell_is_filled():
			m += 1
		if m == 5:
			break
		move_right()

    


if __name__ == '__main__':
    run_tasks()
