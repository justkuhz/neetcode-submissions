"""
key thing here is that we want get and put to run in O(1)
normally simple but since we have a capacity and want to perform LRU, we need to keep track of which elements have been recently accessed and update their order
when we evict we should evict the least recently used element (end of list) and if we access a node by getting or putting it should go to the front of the list
then, since we need a way to perform reordering in O(1) we cant use a hashmap or list to fulfill that as re-ordering those is O(n).

1) We can use a hashmap to store keys and retrieve their values in O(1)
2) We can use a linked list to perform re-ordering in O(1)
--> Hashmap key links to a node in the linked list which holds the value for the key
"""

class ListNode:
    def __init__(self, key: int, val: int, next: ListNode, prev: ListNode):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # init linked list head and tail nodes
        self.head = ListNode(0, 0, None, None)
        self.tail = ListNode(0, 0, None, self.head)
        self.head.next = self.tail

        # init hashmap
        self.cache = {}

        # capacity / current capacity global vars
        self.capacity = capacity
        self.current_capacity = 0

    # in the case that we get or put we will check whether we are inserting a new node or updating an existing ones order
    def access(self, node: ListNode, new: bool) -> None:
        if new:
            # check if we are already capped
            if self.current_capacity == self.capacity:
                self.evict()
            else:
                self.current_capacity += 1
            
        else:
            # remove node from original placement
            node.prev.next = node.next
            node.next.prev = node.prev

        # insert node at front
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    # remove last node in list and delete entry from hashmap
    def evict(self) -> None:
        # point at node to evict
        node = self.tail.prev

        # del cache entry
        del self.cache[node.key]

        # reassign pointers to remove node from linked list
        node.prev.next = self.tail
        self.tail.prev = node.prev

        # delete node
        del node

    def get(self, key: int) -> int:
        # check that key exists
        if key not in self.cache:
            return -1
        
        # key exists, update access
        node = self.cache[key]
        self.access(node, False)
        
        # return value from listnode
        return node.val

    def put(self, key: int, value: int) -> None:
        # check if we are updating a node or creating a new one
        if key in self.cache:
            # point at node to update
            node = self.cache[key]

            # update node val
            node.val = value

            # move node to front of list
            self.access(node, False)
        
        else:
            # create new node
            node = ListNode(key, value, None, None)

            # insert node into cache
            self.cache[key] = node

            # place new node at front of list
            self.access(node, True)
        
