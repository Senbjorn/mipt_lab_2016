#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
	move_down()
	fill()
	for n in range(4):
		move_right(n = 4)
		fill()
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
