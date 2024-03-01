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
    if not isinstance(coins, list):
        raise TypeError("coins must be a list of coin values")
    if not all(isinstance(coin, int) and coin > 0 for coin in coins):
        raise ValueError("coin values must be positive integers")
    if not isinstance(total, int):
        raise TypeError("total must be an integer")
    if total < 0:
        raise ValueError("total cannot be negative")

    if total == 0:
        return 0

    # Create a list to store the minimum number of coins needed for each total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update min_coins list for each possible total
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
