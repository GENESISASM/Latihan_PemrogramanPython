#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    rankings = createRankings(ranked)
    i = len(ranked) - 1
    for score in player:
        flag = True
        while flag:
            if i == -1:
                print(1)
                flag = False
            elif score < ranked[i]:
                print(rankings[i] + 1)
                flag = False
            elif score == ranked[i]:
                print(rankings[i])
                flag = False
            elif score > ranked[i]:
                i -= 1
    return


def createRankings(leaderboard):
    rankings = [1]
    rank = 1
    for i in range(1, len(leaderboard)):
        if leaderboard[i] < leaderboard[i - 1]:
            rank += 1
        rankings.append(rank)
    return rankings


lenOfLeaderboard = int(input())
leaderboard = list(map(int, input().rstrip().split()))
lenOfAliceScores = int(input())
aliceScores = list(map(int, input().rstrip().split()))
climbingLeaderboard(leaderboard, aliceScores)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
