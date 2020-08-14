'''
This was doen for just handson practice to check how to work with 
DP by changing few elements of 0-1 Knapsack problems.
'''
class Solution:    
    def subset(self,nums: List[int],w)->bool:
        n=len(nums)
        t=[[0 for i in range(w+1)]for j in range(n+1)] #Initialising matrix to Save data Top bottom apporoach
        for j in range(w+1):
            t[0][j]=False
        for i in range(n+1):
            t[i][0]=True
        #i goes from 1 to n+1
        #j goes from 0 to w+1
        '''
        This is how the table looks:
        T F F F F F.......w+1
        T
        T
        T
        T
        .
        .
        n+1
        '''
        for i in range(1,n+1):
            print(i,j)
            for j in range(1,w+1):
                if nums[i-1]<=j:
                    t[i][j]=(t[i-1][j-nums[i-1]]) or (t[i-1][j]) #to take th evalue or not
                else:
                    t[i][j]=t[i-1][j] #To not take the value
        return t[n][w] #The final block suggesting is the bigger problem gives a total sum desired