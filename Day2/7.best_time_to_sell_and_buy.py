''''
Best time to buy and sell (Dynamic Programming Question without DP solution) 
Question can be found here:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/

Input:
 prices = [7,1,5,3,6,4]
 
Output:
 5
Explaination:
buy on day 2 (prices=1) and sell  on day 5 (prices = 6)
Profit = 6-1 = 5
Which is max profit
The solution is time complexity of O[n^2] 
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        mini=1000000000
        for  i in range(len(prices)):
            mini=min(mini,prices[i])
            maxi=max(maxi,prices[i]-mini)
        return maxi

