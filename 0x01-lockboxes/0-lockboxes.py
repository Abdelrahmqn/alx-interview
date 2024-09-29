#!/usr/bin/python3
"""LOCK BOXES PROBLEM!"""


def canUnlockAll(boxes):
    """boxes"""
    box_compare = []
    lengthBoxes = len(boxes)
    for i in boxes:
        if len(i) == 0 and i is not boxes[lengthBoxes-1]:
            return False
        for j in i:
            box_compare.append(j)
    print(box_compare)
    for index, keys in enumerate(boxes):
        if index in box_compare or index < lengthBoxes - 1:
            return True
        else:
            return False
