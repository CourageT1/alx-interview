#!/usr/bin/python3
"""a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    Args:
        boxes (list): A list of lists where each list represents a box, and
                      the indices inside the list are the keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    """
    if not boxes or not isinstance(boxes, list):
        return False

    keys = set([0])  # Set to store the box indices that can be unlocked
    stack = [0]      # Stack to perform depth-first search

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in keys and key < len(boxes):
                keys.add(key)
                stack.append(key)

    return len(keys) == len(boxes)
