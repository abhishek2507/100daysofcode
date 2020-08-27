'''
The question can be found out at :

https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/

'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))