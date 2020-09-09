'''
Extension of longest palindromic subsequence problem
Very easy just return len(string)-longestpalnidromicSubsequence
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
Similar problem Catch is if we can make deletion we can even add elements to make a palindrome
'''

class Solution:
    def minDeletionToMakePalindrome(self, x: str) -> int:
        y=x[::-1]
        m=len(x)
        n=len(y)
        t=[[0 for i in range(n+1)]for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (x[i-1]==y[j-1]):
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        return len(x)-t[m][n]
        