"""
Constraints:
How large can this array be?
max 100000 elements in the array
Is the array typed / limited to integers?
array is limited to any integer within 32 bits

I want to try and solve this in one pass O(n) time
I think we can use a set to keep track of values we have already seen, and have O(1)
lookup to check if we are repeating a value or add it into the set
this means O(n) space though in the worst case

This problem falls under arrays since we are iterating over and processing values 
in an array to evaluate some conditions
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # init set
        seen = set()

        # iterate over array
        for num in nums:
            # check if we have seen prev
            if num in seen:
                return True

            # add num to set
            seen.add(num)

        # return 
        return False