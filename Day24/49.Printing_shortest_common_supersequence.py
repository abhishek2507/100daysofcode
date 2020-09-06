'''
Question can be found here :
https://leetcode.com/problems/shortest-common-supersequence/
changes to better understand for future use
LCS is solved below by top bottom approach we will do sma ejust now we wont just keep the LCS element but also keep the non LCS element
And then we iterated the table to find the shortest supersequence
'''
class Solution:
    def shortestCommonSupersequence(self, x, y):
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
        output=""
        while i>0 and j>0:
            if x[i-1]==y[j-1]:
                output+=str(x[i-1])
                i-=1
                j-=1
            else:
                if t[i-1][j]>t[i][j-1]:
                    output+=str(x[i-1])
                    i-=1
                else:
                    output+=str(y[j-1])
                    j-=1
        while i>0:
            output+=x[i-1]
            i-=1
        while j>0:
            output+=y[j-1]
            j-=1
        return output[::-1]