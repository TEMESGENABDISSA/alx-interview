#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    """
    change
    """
    if total <= 0:
        return 0
    matriz = [float('inf')] * (total + 1)
    matriz[0] = 0
    for i in range(len(coins)):
        for j in range(coins[i], total + 1):
            matriz[j] = min(matriz[j], matriz[j - coins[i]] + 1)
    if matriz[total] != float('inf'):
        return matriz[total]
    else:
        return -1
