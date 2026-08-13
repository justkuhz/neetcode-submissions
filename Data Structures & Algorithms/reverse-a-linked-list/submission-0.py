# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
problem domain: linked list / pointers

constraints and notes:
- singly linked list, only next no prev
- list length is 1000 nodes max and can have 0 nodes
- key is to be able to keep track of prev and cur to be able to flip one and then still iterate through original order

approach and complexity:
- we can use two pointers and iterate to the end of the linked list to solve this in one pass and use no extra memory O(n) time O(n) space
- we can use two ptrs, a prev and a cur to flip the order
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            save = curr.next
            curr.next = prev
            prev = curr
            curr = save
        
        return prev
        