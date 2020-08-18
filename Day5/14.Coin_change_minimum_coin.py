'''
Coin change problem for minimum number of coins
https://leetcode.com/problems/coin-change/

This is a very special problem because here 2 rows are initialised
and we used int_max to get maximum integer and then tried going down by minimizing
''' 
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        w=int(amount)
        #n+1 by w+1 table initialised
        int_max=sys.maxsize #used to reference a really great number (Because Python doesnt have a limit for integer.)
        t=[[0 for i in range(w+1)]for j in range(n+1)]
        #Initialising the top row and columns
        for j in range(w+1):
            t[0][j]=int_max-1
        for i in range(1,n+1):
            t[i][0]=0
        #i goes from 1 to n+1
        #j goes from 0 to w+1
        #i itialising the second row
        for j in range(1,w+1):
            if(j%coins[0]==0):
                t[1][j]=j/coins[0]
            else:
                t[1][j]=int_max
        '''
        This is how the table looks:
        0 int_max-1 int_max-1 int_max-1 int_max-1 int_max-1.......w+1
        0 <------This row is also initialied by above logic------>w+1
        0 
        0
        0
        .
        .
        n+1
        '''
        for i in range(2,n+1):
            for j in range(1,w+1):
                if coins[i-1]<=j:
                    #We using min function to get the minimum of the previous sub table
                    t[i][j]=min(1+t[i][j-coins[i-1]] , (t[i-1][j])) #to take the value or not but also keep it available for next time
                else:
                    t[i][j]=t[i-1][j] #To not take the value
        if(int(t[n][w])>=int_max-1):
            return -1 #This checks if the change is even possible
        else:
            return int(t[n][w]) #The final block suggesting is the bigger problem gives a total sum desired 