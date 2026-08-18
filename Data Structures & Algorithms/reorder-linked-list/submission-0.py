# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse second half of linked list
        slow, fast = head, head.next

        # while fast is not null and not at end of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # have second half of list now
        second = slow.next
        slow.next = None
        prev = None

        # reversing the second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # 2 ptrs, one at front of list and other at last element (first element for the reversed list)
        # merge the two lists using alternate re-linking list between the two ptrs

        # head of 2nd half of list
        second = prev
        # head is same
        first = head

        # second half can be shorter than first half
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2



