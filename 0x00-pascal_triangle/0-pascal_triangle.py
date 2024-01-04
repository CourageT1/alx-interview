#!/usr/bin/env python3
"""
a function def pascal_triangle(n)
that returns a list of lists of integers representing the Pascal’s triangle of n:
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Args:
    - n (int): Number of rows for Pascal's triangle.

    Returns:
    - list of lists: Pascal's triangle represented as a list of lists of integers.

    Raises:
    - ValueError: If n is less than or equal to 0.
    """
    if n <= 0:
        raise ValueError("Input should be a positive integer.")

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
