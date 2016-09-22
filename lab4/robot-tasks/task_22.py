#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while True:
    	fill_cell()
    	while not wall_is_on_the_right():
    		move_right()
    		fill_cell()
    	while not wall_is_on_the_left():
    		move_left()
    	if not wall_is_beneath():
    		move_down()
    	else:
    		break


if __name__ == '__main__':
    run_tasks()
