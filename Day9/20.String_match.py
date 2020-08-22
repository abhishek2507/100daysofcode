'''
The question can be found here:
https://www.hackerrank.com/challenges/sparse-arrays

It was mis-labelled as Medium it should be labelled easy.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    res=[]
    for i in range(len(queries)):
        res.append(0)
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                print(queries[i],strings[j])
                res[i]+=1
                print(res)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
