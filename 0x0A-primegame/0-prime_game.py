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
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    prime_count = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    for num in nums:
        if prime_count[num] % 2 == 1:
            maria += 1
        else:
            Ben += 1

    if maria > Ben:
        return 'Maria'
    elif Ben > maria:
        return 'Ben'
    else:
        return None
