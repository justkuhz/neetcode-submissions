"""
Problem domain falls under arrays / list processing

Constraints:
Can numbers be negative? What is our range of numbers here?
any negative/positive integer that can fit in 32 bits
Can we see the same number multiple times in the list?
Yes
How long can the nums list be?
up to 1000 nums in nums list

Approach:
Obvious approach is to sort and count sequence which would be O(nlogn)
time O(n) space

More optimal approach is to store into a set and check for sequence start
O(n) time and O(n) space
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # edge case empty list
        if len(nums) == 0:
            return 0

        # init hash set and res
        res = 1
        seen = set()

        # process nums list into hash set
        for num in nums:
            seen.add(num)


        # work through hash set to count max sequences
        for num in seen:
            if (num - 1) in seen:
                continue
            
            # start of sequence
            run = 1
            while num + 1 in seen:
                run += 1
                num += 1
                res = max(res, run)

        # return max sequence
        return res
        