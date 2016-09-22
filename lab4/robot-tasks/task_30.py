#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    n = 1
    while not wall_is_on_the_right():
    	move_right()
    	n += 1
    while not wall_is_on_the_left():
    	move_left()
    for i in range(n):
    	for j in range(n):
    		if i != j and i + j != n - 1:
    			fill_cell()
    		if j != n - 1:
    			move_right()
    	for j in range(n - 1):
    		move_left()
    	if (i != n - 1):
    		move_down()


if __name__ == '__main__':
    run_tasks()
