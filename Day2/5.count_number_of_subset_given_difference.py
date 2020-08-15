''''
Count total number of Subset equal to a given sum difference (Dynamic Programming solution)
This was just a handson practice for vraitaion in 0-1 Knapsack

Given array nums[] = [1,1,2,3] and difference = 1
Output => 3
Explaination: ([1,1,2],[3]), ([3,1],[1,2]) and ([3,1],[1,2]) #This is second 1 thats why same 2 cases.
Total 3 cases
'''
class Solution:
    def countSubsetGivenDifference(self, nums: List[int],diff: int) -> int:
        #Trick Here is if sum/2 can be made using sub set sum apporach then it can be divided into to 2 equal half
        summer=0
        for i in range(len(nums)):
            summer+=nums[i]
        n=len(nums)
        w=int(summer)
        w=(summer+diff)/2 #s1 partitions at a place where the s1=(sum+diff)/2
        # n+1 by w+1 table initialised
        t=[[0 for i in range(w+1)]for j in range(n+1)]
        #Initialising the top row and columns
        for j in range(w+1):
            t[0][j]=0
        for i in range(n+1):
            t[i][0]=1
        #i goes from 1 to n+1
        #j goes from 0 to w+1
        '''
        This is how the table looks:
        1 0 0 0 0 0.......w+1
        1
        1
        1
        1
        .
        .
        n+1
        '''

        for i in range(1,n+1):
            print(i,j)
            for j in range(1,w+1):
                if nums[i-1]<=j:
                    t[i][j]=(t[i-1][j-nums[i-1]]) + (t[i-1][j]) #to take th evalue or not
                else:
                    t[i][j]=t[i-1][j] #To not take the value
        return t[n][w] #The final block suggesting is the bigger problem gives a total sum desired
