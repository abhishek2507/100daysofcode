'''
Question can be found here :
https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem
changes to better understand for future use
LCS is solved below by top bottom approach
And then we iterated the table to find the longest subsequence
'''
class Solution:
    def printlongestCommonSubsequence(x, y):
        m=len(x)
        n=len(y)
        t=[[0 for i in range(n+1)]for j in range(m+1)]
        print(t)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (x[i-1]==y[j-1]):
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        i=m
        j=n
        index=t[m][n]
        output=[""]*(index+1)
        output[index]=""
        while i>0 and j>0:
            if x[i-1]==y[j-1]:
                output[index-1]=str(x[i-1])
                i-=1
                j-=1
                index-=1
            else:
                if t[i-1][j]>t[i][j-1]:
                    i-=1
                else:
                    j-=1
        return output