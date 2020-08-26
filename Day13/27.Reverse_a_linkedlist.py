'''
The question can be found at:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev= None
        itr=head
        while(itr):
            nxt = itr.next
            itr.next= prev
            prev = itr
            itr=nxt
        head=prev
        return head