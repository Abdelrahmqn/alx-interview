#!/usr/bin/python3
"""Pascal's Triangle Module
This module contains a function that generates Pascal's triangle.
The triangle is represented as a list of lists, where each inner list
contains the numbers corresponding to a row in Pascal's triangle.
"""


def pascal_traingle(n):
    """
    Pascal's Traingle implementation

    parameters: (n)
    returns: a row (list)

    [0, 1, 0]
    [0 + 1, 1, 0 + 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    """
    if not isinstance(n, int):
        raise TypeError("n Must be an integer!")
    if n <= 0:
        return []

    res = [[1]]
    for i in range(n - 1):
        temp = [0] + res[-1] + [0]  # [0, 1, 0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
        print(row)
