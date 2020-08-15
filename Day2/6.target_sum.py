''''
Target Sum (Dynamic Programming solution)
Question can be found here:
https://leetcode.com/problems/target-sum/

Input:
 nums = [1, 1, 2, 3]
 target = 1
Output:
 3
Explaination:
 Subset1 = {+1,-1,-2,+3}
 Subset2 = {-1,+1,-2,+3}
 Subset3 = {+1,+1,+2,-3}
 Difference = 1 (Which is Target Sum)

 Trick:
    Divide it in 2 halves
            |      |
        {+1,+3}  {-1,-2}
        Can we say we divide 2 subset to reach a given difference ?
        Similar to Code #5 count_number_of_subset_given_difference.py
        We need to make few changes:
            To reach desired goal due to multiple 0s case:
            Change #1 Start cols from 0s and not from 1 (for j in range(0,w+1))
            Change #2 Because we are starting from 0 we need to manage edge cases of 0s manually
            by checking:
            if the target_sum > total_sum_of_array or (target_sum+total_sum_of_array) is odd:
                Return 0

'''
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        summer=0
        zeros=0
        for i in range(len(nums)):
            summer+=nums[i]
        
        if S > summer or (summer+S)%2!=0: #If the S=odd and 
            return 0
        n=len(nums)
        w=int((summer+S)/2) #s1 partitions at a place where the s1=(sum+diff)/2
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
            for j in range(0,w+1): #Here we made some initialization changes and starting from start because cases with multiple 0s exists so even the 0s have to be solved
                if nums[i-1]<=j:
                    t[i][j]=(t[i-1][j-nums[i-1]]) + (t[i-1][j]) #to take th evalue or not
                else:
                    t[i][j]=t[i-1][j] #To not take the value
        return t[n][w] #The final block suggesting is the bigger problem gives a total sum desired
