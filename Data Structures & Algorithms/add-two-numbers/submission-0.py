# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
important to note that l1 can be a different length than l2
we can iterate through both pointers and keep track of a carry
O(m+n) time and O(1) extra space
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node for return
        dummy = ListNode()
        cur = dummy

        # carry over
        carry = 0

        # continue while we have any numbers left
        while l1 or l2 or carry:
            # collect our two integers if we can
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            # carry is 1 or 0 depending on val >= 10
            carry = val // 10
            # val is mod 10 so it stays <= 9
            val = val % 10
            # create new listnode and append to result list
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            # move l1 and l2 ptrs if we can
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


            