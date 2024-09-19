#!/usr/bin/python3
"""pascal's traingle"""

from typing import List


def pascal_traingle(n: int):
    """pascal's traingle in [0, x, 0] way"""
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
