'''
problem domain: lists/arrays, sorting, binary search

approach and complexity:
ideally time O(logn), we want to try and apply binary search even though its been rotated
as a result of the rotate, there will be a left sorted array and a right sorted array
we will determine the middle and shift our search to the left or right of mid depending on
whether the middle element falls in the left sorted array or right sorted array
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # init ptrs and res
        l, r = 0, len(nums) - 1
        res = nums[0]

        # search, we do inclusive since min element could be the very first or very last element
        while l <= r:
            # update min
            if nums[l] < nums[r]:
                res = min(res, nums[l])

            mid = l + (r - l) // 2
            res = min(res, nums[mid])

            # if we are part of left sorted array, search right
            if nums[mid] >= nums[l]:
                l = mid + 1
            else: # we are in right sorted array, search left
                r = mid - 1
        
        return res
            
            


        