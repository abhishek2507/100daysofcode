'''
Question can be found out at :
https://www.interviewbit.com/problems/repeating-subsequence/
'''
class Solution:
    def anytwo(self,x):
        y=x
        m=len(x)
        n=len(y)
        t=[[0 for i in range(n+1)]for j in range(m+1)]
        print(t)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (x[i-1]==y[j-1]) and (i!=j): #Just one condition dont take same index in the same string
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        if t[m][n]>1:
            return 1
        else:
            return 0