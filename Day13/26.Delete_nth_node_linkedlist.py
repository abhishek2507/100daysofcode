'''
The question can be found at:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        itr=head
        total_count=0
        while(itr):
            total_count+=1
            itr=itr.next
        index=total_count-n
        print(index)
        itr=head
        count=0
        if(n==total_count):
            return head.next
        while(itr):
            if count == index-1:
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
        return head