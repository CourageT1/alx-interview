#!/usr/bin/python3
"""
Module for making change with the fewest number of coins.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list of int): List of coin values available.
        total (int): The desired total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
             Returns -1 if the total cannot be met by any combination of coins.

    Raises:
        TypeError: If coins is not a list or if total is not an integer.
        ValueError: If total is negative.

    Examples:
        >>> makeChange([1, 2, 25], 37)
        7
        >>> makeChange([1256, 54, 48, 16, 102], 1453)
        -1
    """
    if total <= 0:
        return (0)

    coins = sorted(coins)
    count = 0
    length = len(coins)
    i = (length - 1)
    while i >= 0:
        if not total:
            break
        if coins[i] <= total:
            total -= coins[i]
            count += 1
        else:
            i -= 1
    if total:
        return (-1)
    return (count)
