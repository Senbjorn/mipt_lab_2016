#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
	b = True
	while True:
		b = False
		while not wall_is_on_the_right():
			if not wall_is_beneath():
				b = True
				break
			move_right()
		while not wall_is_on_the_left():
			if not wall_is_beneath():
				b = True
				break
			move_left()
		if not b:
			break
		move_down()



if __name__ == '__main__':
    run_tasks()
