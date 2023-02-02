'''Sudoku Solver'''


# generate a 9x9 grid
grid = [[0 for x in range(9)] for y in range(9)]

# solve the sudoku
def solve(grid):
    # find empty cell
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1,10):
                    # check if n is valid at (x,y)
                    if is_valid(grid, x, y, n):
                        grid[x][y] = n
                        # recursive call to solve remaining cell
                        if solve(grid):
                            return True
                        else:
                            # backtrack if the solution does not work
                            grid[x][y] = 0
                return False
    return True

def is_valid(grid, x, y, n):
    # all rows
    for i in range(9):
        if grid[x][i] == n:
            return False
    # all columns
    for i in range(9):
        if grid[i][y] == n:
            return False
    # all 9 small grids
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[x0+i][y0+j] == n:
                return False
    return True

if __name__ == '__main__':
    # example sudoku
    grid = [[0, 9, 3, 4, 2, 7, 5, 0, 0],
            [0, 0, 7, 0, 1, 5, 3, 0, 0],
            [0, 2, 4, 6, 8, 0, 0, 0, 7],
            [3, 0, 0, 7, 6, 0, 2, 1, 9],
            [6, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 3, 0, 0, 0, 0],
            [4, 0, 5, 8, 0, 0, 9, 2, 6],
            [0, 0, 1, 2, 0, 6, 0, 7, 3],
            [0, 7, 0, 0, 0, 9, 8, 0, 0]]
    solve(grid)
    # print the solved sudoku
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
