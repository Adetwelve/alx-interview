#!/usr/bin/python3

def check_fuct(grid):
    gridlen = len(grid)
    for element in grid[0]:
        if element != 0:
            return False

    for element in grid[-1]:
        if element != 0:
            return False

    for ele in range(1, gridlen-1):
        if grid[ele][0] == 1:
           return False

        if grid[ele][-1] == 1:
            return False
    return True




if __name__ == '__main__':

    grid = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0]
         ]
    print(check_fuct(grid))
