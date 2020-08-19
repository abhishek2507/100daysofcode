'''
The question can be found at :
https://leetcode.com/problems/partition-to-k-equal-sum-subsets

Input1:
nums=[4,3,2,3,5,2,1]
k=4
Output1= True

Input2:
nums=[4,3,2,3,5,2]
k=4
Output1= False

I am trying to master Recursion from scratch from past few days, so the total # of question has decreased
But will start uploading a lot more questions as soon i complete my tutorials n practice 
'''

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Total sum of our array
        ts = sum(nums)
        # If there's a remainder here we know nums k totals aren't
        # going to be rounded sums.
        if ts % k != 0:
            return False
        # Individual total sum, for each subset.
        its = int(ts/k)
        # We need to keep track of nums that we use.
        used = [False] * len(nums)
        # Sort in desc order to help the efficiency.
        nums.sort(reverse=True)
        def helper(t, k, idx):
            # If k == 0 we have satisfied our base case and filled all subsets.
            if k == 0:
                return True
            # If t == 0, our current subset satisfies our target.
            if t == 0:
                # deduct 1 from k seeing as we just found a subset.
                # Recurse starting at idx 0 again.
                return helper(its, k - 1, 0)
            else:
                # We keep searching for numbers.
                for i in range(idx, len(nums)):
         # if we haven't used nums[i] and t - nums[i] doesn't take our total to negatives.
                    if not used[i] and t - nums[i] >= 0:
                        # Mark num[i] as used
                        used[i] = True
                        # recurse and try to find next number.
                        # if successful we'll return true
                        if helper(t - nums[i], k, i + 1):
                            return True
                        # If we cant find an additional number using nums[i], we mark
                        # back to False and keep going. 
                        used[i] = False

        return True if helper(its, k, 0) else False