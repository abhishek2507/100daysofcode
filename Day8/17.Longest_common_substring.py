'''
Question can be found here :
https://practice.geeksforgeeks.org/problems/longest-common-substring/0
changes to better understand for future use
Longest common substring is solved below by top bottom approach
'''
class Solution:
    def longestCommonSubstring(self, x: str, y: str) -> int:
        m=len(x)
        n=len(y)
        t=[[0 for i in range(n+1)]for j in range(m+1)]
        print(t)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (x[i-1]==y[j-1]):
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=0 #change no 1 we will reset the longest to zero
        maxi=0
        for i in range(m+1):
            for j in range(n+1):
                if t[i][j]>maxi:
                    maxi=t[i][j]
        return maxi
            