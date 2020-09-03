'''

This problem is a very famous problem known as minimum insertion and deletion to reach string a to string b
If we add "Replace" function to it becomes minimum distacne problem
https://leetcode.com/problems/delete-operation-for-two-strings

'''

class Solution:
    def minDistance(self, x: str, y: str) -> int:
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
        return (len(x)+len(y)-2*t[m][n]) #Take the lcs n find difference betweenit and the other 2 string
        