#!/usr/bin/python3

import pyrob.core as rob
from pyrob.tasks import check_filled_cells, find_cells_to_be_filled
import random


class Task:
    CHECKS = 5

    def load_level(self, n):
        n = random.randint(20, 30)
        rob.set_field_size(10, 10)

        cases = {
            0: {'top': True},
            1: {'bottom': True},
            2: {'top': True},
            3: {'bottom': True}
        }

        rob.goto(2, 0)
        for i in range(10):
            for j in range(10):
                rob.goto(i, j)
                case = random.randint(0, 3)
                rob.put_wall(**cases[case])
            # if not rob.wall_is_above():
            #     rob.set_cell_type(1, j, rob.CELL_TO_BE_FILLED)

            # if not rob.wall_is_beneath():
            #     rob.set_cell_type(3, j, rob.CELL_TO_BE_FILLED)

        self.cells_to_fill = find_cells_to_be_filled()

        rob.set_parking_cell(2, n-1)

        rob.goto(2, 0)

    def check_solution(self):

        return check_filled_cells(self.cells_to_fill) and rob.is_parking_point()