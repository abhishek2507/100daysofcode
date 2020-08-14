''''
Equal Subset Problem (Dynamic Programming solution)
Question can be found here:
https://leetcode.com/problems/partition-equal-subset-sum/
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summer=0
        for i in range(len(nums)):
            summer+=nums[i]
        #Trick Here is if sum/2 can be made using sub set sum apporach then it can be divided into to 2 equal half
        if summer%2==0: #Cgecking if the sum is Even to proceed else return False
            n=len(nums)
            w=int(summer/2)
            #n+1 by w+1 table initialised
            t=[[0 for i in range(w+1)]for j in range(n+1)]
            #Initialising the top row and columns
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
        else:
            return False #If its odd