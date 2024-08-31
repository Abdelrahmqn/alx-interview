#!/usr/bin/env python3
from sys import argv as arg
"""
python documenation
"""


def n_queens():
    n = arg[1]

    if len(arg) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(arg[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = []

    def backtracking(r):
        if r == n:
            res.append(board[:])
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board.append([r, c])

            backtracking(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board.pop()

    backtracking(0)
    for solution in res:
        print(solution)


n_queens()
