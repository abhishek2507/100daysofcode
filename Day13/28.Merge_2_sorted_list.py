'''
The question can be found at:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(0)
        potr=head
        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                potr.next=l2
                break
            elif l2 is None:
                potr.next=l1
                break
            else:
                small_num=0
                if l1.val<l2.val:
                    small_num=l1.val
                    l1=l1.next
                else:
                    small_num=l2.val
                    l2=l2.next
                    
                newNode = ListNode(small_num)
                potr.next=newNode
                potr=potr.next
            
        return head.next