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


def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_sieve(limit):
    """
    Generate all prime numbers up to a given limit using the Sieve of
    Eratosthenes algorithm.

    Args:
        limit (int): The upper limit for prime number generation.

    Returns:
        list: A list of prime numbers up to the specified limit.
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [num for num in range(limit + 1) if sieve[num]]


def simulate_game(n):
    """
    Simulate a single round of the game for a given set of consecutive
    integers up to n.

    Args:
        n (int): The upper limit of the set of consecutive integers.

    Returns:
        str: The name of the player who wins the game ('Maria' or 'Ben').
    """
    primes = prime_sieve(n)
    num_primes = len(primes)
    if num_primes % 2 == 0:
        return "Ben"
    else:
        return "Maria"


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
