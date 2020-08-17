'''
Rod cutting problem is the best example of Unbounded Knapsack
It would be a shame if we dont include this old and evergreen problem by doing Dynamic programming

''' 
class Solution:
    def rodcutting(self,length_array,price,total_length)->int:
        n=len(length_array)
        w=int(total_length)
        #n+1 by w+1 table initialised
        t=[[0 for i in range(w+1)]for j in range(n+1)]
        #Initialising the top row and columns
        for j in range(w+1):
            t[0][j]=0
        for i in range(n+1):
            t[i][0]=0
        #i goes from 1 to n+1
        #j goes from 0 to w+1
        '''
        This is how the table looks:
        0 0 0 0 0 0.......w+1
        0
        0
        0
        0
        .
        .
        n+1
        '''
        for i in range(1,n+1):
            print(i,j)
            for j in range(1,w+1):
                if length_array[i-1]<=j:
                    t[i][j]=max(price[i-1]+t[i][j-length_array[i-1]] , (t[i-1][j])) #to take the value or not
                else:
                    t[i][j]=t[i-1][j] #To not take the value
        return t[n][w] #The final block suggesting is the bigger problem gives a total sum desired
        