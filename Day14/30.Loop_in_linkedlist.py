'''

The question can be found out at:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/

'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        lisi={}
        pos=0
        itr=head
        while(itr):
            if itr in lisi:
                return True
            lisi[itr]=itr
            itr=itr.next
        return False
            