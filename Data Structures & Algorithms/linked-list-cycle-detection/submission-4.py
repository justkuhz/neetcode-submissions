# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
floyds fast slow cycle detection
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next

            if fast and slow and fast == slow:
                return True
        
        return False
        