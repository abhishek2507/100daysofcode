'''
The question can be found out at :

https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.bsthelp(root,-1000000000000,100000000000)
    def bsthelp(self,root,mini,maxi):
        if root is None:
            return True
        if root.val<=mini or root.val>=maxi:
            return False
        validleft=self.bsthelp(root.left,mini,root.val)
        validright=self.bsthelp(root.right,root.val,maxi)
        return validleft and validright
