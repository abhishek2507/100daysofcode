class Solution:
    def longestcommonsubstring(self, x: str,y: str) -> str:
        m=len(x)
        n=len(y)
        t=[[0 for i in range(n+1)]for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (x[i-1]==y[j-1]):
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=0 #Same code as Longest common substring we just iterate diagonally to find the string
        max_i,max_j=0,0
        maxi=0
        for i in range(m+1):
            for j in range(n+1):
                if t[i][j]>maxi:
                    maxi=t[i][j]
                    max_i=i #storing value of the cell with longest common substring value
                    max_j=j
        final=['0']*maxi
        #Then we start iterating it diagonally 
        while t[max_i][max_j]!=0:
            maxi-=1
            final[maxi]=x[max_i-1] #we can even take y[max_j-1]
            max_i-=1
            max_j-=1
        return (''.join(final))