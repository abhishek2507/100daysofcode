'''
The question can be found at:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/
'''
class Solution:
    def deleteNode(self, node):
        if node.next is not None:
            node.next,node.val = node.next.next,node.next.val