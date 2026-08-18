# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
two passes, one to find length of list and second to remove n from end
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next

        # we have length now
        remove = length - n

        # edge case we remove front element
        if remove == 0:
            return head.next

        cur = head
        for i in range(length - 1):
            if (i + 1) == remove:
                cur.next = cur.next.next
                break
            cur = cur.next
        
        return head


        