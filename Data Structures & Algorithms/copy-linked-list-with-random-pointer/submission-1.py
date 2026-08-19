"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
we can copy the list without using extra space by interleaving copied nodes inside the original list
A -> B -> C becomes A -> A' -> B -> B' -> C -> C'

For each original node we can create a copy and insert it right after
For each original node if the random exists then we can set the random on the copy as well
Once the above is done, we can restore the original list and extract all copies into a new separate list
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # handle empty list case
        if head is None:
            return None

        # create copies with vals and append right after
        l1 = head
        while l1 is not None:
            # create initial copy with val A'
            l2 = Node(l1.val)
            # insert it inbetween A and B
            l2.next = l1.next
            l1.next = l2
            # skip A' straight to B
            l1 = l2.next

        newHead = head.next

        # assign random pointers
        l1 = head
        while l1 is not None:
            if l1.random is not None:
                # A'.random = A.random.next (point A' at the respective deep copy of A.random)
                l1.next.random = l1.random.next

            # skip ptr over A' straight to B
            l1 = l1.next.next 

        # restore original and new list
        l1 = head
        while l1 is not None:
            # l2 = A'
            l2 = l1.next
            # A.next = A'.next = B
            l1.next = l2.next
            # set A'.next to be B' as long as there are more nodes after
            if l2.next is not None:
                l2.next = l2.next.next
            
            # l1 pointing at B now
            l1 = l1.next

        # return A' (deep copy of head)
        return newHead
