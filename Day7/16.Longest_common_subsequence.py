'''
Question can be found here :
https://leetcode.com/problems/longest-common-subsequence/
changes to better understand for future use
LCS is solved below by top bottom approach
'''
class Solution:
    def longestCommonSubsequence(self, x: str, y: str) -> int:
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
        return t[m][n]