'''
The question can be found out at :

https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr=sorted(arr)
    mini=1000000000
    for i in range(len(arr)-1):
        mini=min(abs(arr[i]-arr[i+1]),mini)
    return mini
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()