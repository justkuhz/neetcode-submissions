"""
constraints:
how long can the nums list be?
at most 1000 elements in list

is there a possibility of no solutions or empty list?
one valid answer exists in every case (never empty list)

how should i handle if there are multiple solutions?
answered above

approach:
we can solve this in one pass and use a hashmap to keep track of previous values we've seen and
the index we saw them at. As we see new values we will evaluate whether we meet the two sum
condition or not.

One pass = O(n) time
hash map = O(n) space

post problem thoughts:
This problem tests both our ability to iterate and process arrays as well as using hashmaps 
to evaluate and solve for a given condition
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # init hash map and res
        seen = {}

        # iterate over nums
        for i in range(len(nums)):
            # check if valid complement in hashmap
            complement = target - nums[i]
            if (complement) in seen:
                return [seen[complement], i]

            # insert current value/index into hashmap
            seen[nums[i]] = i

        