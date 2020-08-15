''''
Minimum difference subsets (Dynamic Programming solution)
Question can be found here:
https://www.interviewbit.com/problems/minimum-difference-subsets/

Input:
 nums = [1, 6, 11, 5]
Output:
 1
Explaination:
 Subset1 = {1, 5, 6}, sum of Subset1 = 12
 Subset2 = {11}, sum of Subset2 = 11 
 Difference = 1 (this is minimum difference)
'''
class Solution:
    def solve(self,nums):
        n=len(nums)
        w=0
        for i in range(len(nums)):
            w+=nums[i]
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
        #Here the last row of t[][] suggesting the possible sums can be achieved by using these numbers
        s1=[] #Selecting appropriate sums whihc can be achieved by this set of number using subset sum
        for i in range(w//2+1):
            if t[n][i]==True:
                s1.append(i)
        mini=100000
        for i in range(len(s1)):
            mini=min(mini,w-2*s1[i]) #If we get s1, s2 = total-s1, so difference will be total-2*s1
        return mini

