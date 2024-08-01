#!/usr/bin/python3
"""
Module for a method that determines if all the boxes in a list can be unlocked.
"""
def canUnlockAll(boxes):
    """
    Determines if all the boxes in the list can be unlocked.

    Args:
        boxes (list): A list of lists representing the lockboxes
        and their corresponding keys.

    Returns:
      bool: True if all the boxes can be unlocked, False otherwise.
    """

    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    # crate stack to store boxes for exploration
    stack = [0]
    # depth-first search to visit boxes

    while stack:
        current = stack.pop()
        #iterate keys in current box
        for key in boxes[current]:
            # check if key is valid and not visited yet
            if key < n and not visited[key]:
                # mark as visited
                visited[key] = True
                # append to stack
                stack.append(key)

    # returns true if all boxes checked and opened
    return all(visited)
