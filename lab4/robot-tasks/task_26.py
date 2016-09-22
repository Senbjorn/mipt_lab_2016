#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
	for m in range(5):
		fill()
		for k in range(9):
			move_right(n = 4)
			fill()
		for k in range(9):
			move_left(n = 4)
		if m != 4:
			move_down(n = 4)

def fill():
	move_down()
	fill_cell()
	move_right()
	fill_cell()
	move_right()
	fill_cell()
	move_left()
	move_up()
	fill_cell()
	move_down(n = 2)
	fill_cell()
	move_up()
	move_left()
	move_up()


if __name__ == '__main__':
    run_tasks()
