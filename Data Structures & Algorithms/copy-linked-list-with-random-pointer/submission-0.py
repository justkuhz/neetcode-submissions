"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # default to new node thats empty
        oldToCopy = collections.defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        # one pass over elements in list
        cur = head

        while cur:
            # create / update node val
            oldToCopy[cur].val = cur.val
            # create / update node next
            oldToCopy[cur].next = oldToCopy[cur.next]
            # create / update node random
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next
        
        # return head of deep copy
        return oldToCopy[head]