'''

Coin change Problem maximum way to reach a sum(Dynamic Programming solution)

Question can be found here:
https://www.hackerrank.com/challenges/coin-change/problem
https://practice.geeksforgeeks.org/problems/coin-change/0

Very important question from interview point of view

'''

#!/bin/python3

import math
import os
import random
import re
import sys

def getWays(summer, nums):
        n=len(nums)
        w=int(summer)
        #n+1 by w+1 table initialised
        t=[[0 for i in range(w+1)]for j in range(n+1)]
        #Initialising the top row and columns
        for j in range(w+1):
            t[0][j]=0
        for i in range(n+1):
            t[i][0]=1
        #i goes from 1 to n+1
        #j goes from 0 to w+1
        '''
        This is how the table looks:
        1 0 0 0 0 0.......w+1
        1
        1
        1
        1
        .
        .
        n+1
        '''

        for i in range(1,n+1):
            print(i,j)
            for j in range(1,w+1):
                if nums[i-1]<=j:
                    t[i][j]=(t[i][j-nums[i-1]]) + (t[i-1][j]) #to take th evalue or not
                else:
                    t[i][j]=t[i-1][j] #To not take the value
        return t[n][w] #The final block suggesting is the bigger problem gives a total sum desired
#
# Complete the 'getWays' function below.
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
