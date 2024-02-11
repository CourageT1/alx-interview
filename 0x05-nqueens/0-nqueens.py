#!/usr/bin/python3
"""
Module: nqueens

This module contains functions to solve the N queens problem.
"""

import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen in a given position on the board.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.
        N (int): The size of the board.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solve the N queens problem.

    Args:
        N (int): The size of the chessboard.

    Returns:
        list: A list of solutions, where each solution is represented as a
        list of queen positions.
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []

    def solve_util(board, row):
        if row == N:
            solutions.append([(
                r, c) for r in range(N) for c in range(N) if board[r][c] == 1])
            return True

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve_util(board, row + 1)
                board[row][col] = 0

    solve_util(board, 0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
