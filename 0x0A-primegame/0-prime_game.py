#!/usr/bin/python3
"""PRIME GAME.
"""


def isWinner(x, nums):
    """THE WINNER OF PRIME GAME.
    """
    if x < 1 or not nums:
        return None
    maria, Ben = 0, 0

    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        Ben += primes_count % 2 == 0
        maria += Ben % 2 == 1
    if maria == Ben:
        return None
    if maria > Ben:
        return 'Maria'
    return 'Ben'
