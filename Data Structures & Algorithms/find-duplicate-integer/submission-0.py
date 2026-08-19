"""
we can treat this list of numbers as nodes with edges and guarantee a cycle exists if there is a repeated number (two entry points to the same node). we can use fast and slow ptrs to find the entry of the cycle, and then another single step pointer to meet at the duplicate number

O(n) time and O(1) space without manipulating array
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # traverse by calling nums[ptr] or nums[nums[ptr]] instead of .next
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                # cycle, but not necessarily the repeated number
                break

        # slow is not stuck in the cycle moving back and forth
        slow2 = 0
        while True:
            slow = nums[slow]
            # slow2 eventually catches up and meets slow at the repeated number
            slow2 = nums[slow2]
            if slow == slow2:
                return slow