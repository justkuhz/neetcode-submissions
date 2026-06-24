'''
problem domain: lists/pointers/hashing/sorting

This problems seems impossible to do in O(n) so it would be wise to sort O(nlogn) to have an
easier time processing the list

we can use two pointers to fix one number and search for the other two. we can move our 
pointers in a predictable way since it is sorted

time complexity would be O(n^2) and space complexity would be O(1) plus overhead for sorting
and result list output

constraints:
is nums guaranteed to be populated?
yes, minimum 3 elements
how long is nums?
max 1000 elements
range of integer values in nums?
-100000 to 100000, will never go out of bounds of 32 bit integer

key insight:
sorting will help make the problem more optimized and help with the logic
we already know its not possible to solve in one pass or do more efficiently than O(n^2) due
to having to check three different variables
by being able to lock one down and properly skip duplicates we can optimize from O(n^3) to
O(n^2)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result list and sort nums list
        res = []
        nums.sort()

        # iterate over nums
        for i, a in enumerate(nums):
            # edge case, if first num is greater than 0, its impossible to satisfy the condition
            # of a + b + c == 0 since b/c guaranteed to be greater than a
            if a > 0:
                break

            # skip duplicates
            if i > 0 and a == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            # shift pointers for each iteration
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1

                elif threeSum < 0:
                    l += 1

                else: # threeSum == 0
                    res.append([a, nums[l], nums[r]])

                    # skip duplicates further duplicates
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res



