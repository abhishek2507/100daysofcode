'''
Sherlock and valid String

Question can be found here:
https://www.hackerrank.com/challenges/sherlock-and-valid-string

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    lisi=[]
    max_oc=0
    res=-1
    count=0
    Hash = dict();
    Compar = dict();
    #Storing all the String data in Hashmap
    for i in range(len(s)):
        if s[i] in Hash.keys():
            Hash[s[i]]+=1
        else:
            Hash[s[i]]=1;
    
    #Making a list to Keep all the value data
    for i in Hash:
        lisi.append(Hash[i])

    #transfering list to second hashmap
    for i in range(len(lisi)):
        if lisi[i] in Compar.keys():
            Compar[lisi[i]]+=1
        else:
            Compar[lisi[i]]=1
    
    #Finding maximum occurence
    for i in Compar:
        if(max_oc<Compar[i]):
            max_oc=Compar[i]
            res=i
    #Cases
    for i in Hash:
        if(Hash[i]!=res):
            if(Hash[i]>3):
                count+=1
            count+=1
    if count>1:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(str(result)+ '\n')

    fptr.close()
