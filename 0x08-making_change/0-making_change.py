#!/usr/bin/python3
"""
MAKE CHANGE
"""


def makeChange(coins, total):
    """
    MINIMUM COINS
    """
    if total <= 0:
        return 0
    TRACING, COUNT = 0, 0
    coins.sort()
    coins = coins[::-1]
    while len(coins) > 0:
        VAL = coins[0]
        if TRACING + VAL > total:
            coins.pop(0)
            continue
        TRACING += VAL
        COUNT += 1
        if TRACING == total:
            return COUNT
    return -1
