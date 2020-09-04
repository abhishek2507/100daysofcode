'''
Very simple problem with using LCS to determine the common part in a string and its reversed half.
The problem can be found out at:
https://leetcode.com/problems/longest-palindromic-subsequence
'''



class Solution:
    def longestPalindromeSubseq(self, x: str) -> int:
        y=x[::-1] #Just reverse the original string to obtain the second half
        m=len(x)
        n=len(y)
        t=[[0 for i in range(n+1)]for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (x[i-1]==y[j-1]):
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        return t[m][n]