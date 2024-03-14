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
    Determine the winner of multiple rounds of the game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of integers representing the upper limit for
        each round.

    Returns:
        str or None: The name of the player who won the most rounds
        ('Maria' or 'Ben').
                     Returns None if the winner cannot be determined.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
