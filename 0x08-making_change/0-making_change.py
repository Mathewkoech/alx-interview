#!/usr/bin/python3
"""
Making Change"""
def makeChange(coins, total):
    """Given a pile of coins of different values, 
    determine the fewest number of coins needed to meet a given amount total."""
    if total <= 0:
        return 0
    coins.sort(reverse=True) # sort coins in descending order
    change = 0
    for coin in coins: # iterate through coins
        while total >= coin:
            total -= coin
            change += 1
    if total != 0:
        return -1
    return change

