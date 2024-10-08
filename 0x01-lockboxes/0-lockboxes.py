#!/usr/bin/python3
"""LOCK BOXES PROBLEM!"""


def join(b, T):
    """join"""
    res = []
    for e in T:
        res += b[e]
    return res


def canUnlockAll(boxes):
    """LOCK BOXES"""
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True
    return len(total) == len(boxes)
