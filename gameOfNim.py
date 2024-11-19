"""
Alice and Bob take turns playing a game with Alice starting first
There are n piles of stones. On each player's turn, the player should remove any positive number of stones from a non empty pile of his or her choice
The first player who cannot make a move loses, and the other player wins.
Given an integer array piles, where piles[i] is the number of stones in the ith pile, return true if Alice wins, or false if Bob wins.
"""
def nimGame(piles):
    nimsum = 0
    for p in piles:
        nimsum ^= p
    return nimsum != 0

piles = [1]
print(nimGame(piles))
piles = [1, 1]
print(nimGame(piles))
