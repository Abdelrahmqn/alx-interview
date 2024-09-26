#!/usr/bin/python3
"""ISLAND PERIMETER"""


def island_perimeter(grid):
    """Island Perimeter Problem implementation"""

    rows, cols = len(grid), len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2
                if j < cols - 1 and grid[i][j + 1]:
                    perimeter -= 2
    return perimeter
