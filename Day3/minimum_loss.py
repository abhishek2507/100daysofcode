'''
Minimum Loss

Question can be found here:
https://www.hackerrank.com/challenges/minimum-loss/

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    nums = list(price)
    nums.sort()
    minCost = 10**10
    for i in range(1,n):
        if (nums[i]-nums[i-1] < minCost)  and (price.index(nums[i]) < price.index(nums[i-1])):
                minCost = nums[i]-nums[i-1]
    return minCost
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()

