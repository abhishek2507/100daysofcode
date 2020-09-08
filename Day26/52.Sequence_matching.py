'''
Sequence pattern matching
x=abc
y=adcbedc
output= True

y=abc
y=acbdeba
output= False
'''
class Solution:
    def SequencePatternMatching(self, x: str, y: str) -> int:
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
        if t[m][n]==len(x) or t[m][n]==len(y):
            return True
        else:
            return False