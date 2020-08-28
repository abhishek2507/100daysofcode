'''
The problem can be found here:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/

'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        result = []
        if root == None:
            return
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(level)
        return result
