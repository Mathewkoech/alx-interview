#!/usr/bin/env python3

"""Prime Game Module"""
def isWinner(x, nums):
    """returns the name of the player that won the most rounds"""
    if not nums or x < 1:
        return None
    n = max(nums)
    filters =[True for _ in range(n + 1)]
    filters[0] = filters[1] = False
    for i in range(2, n + 1):
        if filters[i]:
            for j in range(i * i, n + 1, i):
                filters[j] = False
    filters[0] = False
    filters[1] = False
    c = 0
    for i in range(2, n + 1):
        if filters[i]:
            c += 1
        filters[i] = c
    player1 = 0
    for n in nums:
        player1 += filters[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
