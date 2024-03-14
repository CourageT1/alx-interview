#!/usr/bin/python3
"""
This script determines the winner of a game where two players take turns
choosing prime numbers from a set
of consecutive integers and removing their multiples until no more moves can
be made. The player who cannot
make a move loses the game. The script simulates multiple rounds of the game
and determines the player who
wins the most rounds.

Author: Talent

"""


def SieveOfEratosthenes(n):
    """
    Implementing the Sieve of Eratosthenes algorithm to find prime numbers.

    Args:
        n (int): The upper limit for finding prime numbers.

    Returns:
        int: The count of prime numbers up to the given limit.
    """
    # Initialize a list to mark numbers as prime or not
    prime = [True for i in range(n+1)]
    p = 2
    result = 0

    # Loop through numbers until the square root of n
    while (p * p <= n):
        if (prime[p] is True):
            # Mark multiples of prime numbers as not prime
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Count the number of primes
    for p in range(2, n+1):
        if prime[p]:
            result += 1
    return result


def isWinner(x, nums):
    """ 
    Determine the winner of multiple rounds of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of integers representing the upper limit for
        each round.
    Returns:
        str or None: The name of the player who won the most rounds
        ('Maria' or 'Ben').
                     Returns None if the winner cannot be determined.
    """
    # Initialize counters for Maria's and Ben's wins
    b_win, m_win = 0, 0

    # If no rounds, return None
    if not x:
        return None

    # Iterate through each round
    for i in range(x):
        # Count primes using Sieve of Eratosthenes
        primes = SieveOfEratosthenes(nums[i])
        # Determine winner of the round based on the count of primes
        if primes % 2 == 0:
            b_win += 1
        else:
            m_win += 1

    # Compare wins and determine overall winner
    if b_win > m_win:
        return "Ben"
    elif m_win > b_win:
        return "Maria"
    else:
        return None
