'''
The question can be found out at:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lisi=[]
        prev=None
        itr=head
        while itr:
            lisi.append(itr.val)
            itr=itr.next
        itr=head
        while itr:
            nxt=itr.next
            itr.next=prev
            prev=itr
            itr=nxt
        head=prev
        itr=head
        for i in range(len(lisi)):
            if lisi[i] != itr.val:
                return False
            itr=itr.next
        return True
            