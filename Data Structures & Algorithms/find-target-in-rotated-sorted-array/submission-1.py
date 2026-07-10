'''
problem domain: lists/arrays, sorting, binary search

approach and complexity:
1) find pivot to distinguish between sorted left and right half O(logn) time
2) perform normal binary search on each half, and return -1 if not found in either

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init ptrs
        l, r = 0, len(nums) - 1

        # find pivot
        while l < r:
            mid = l + (r - l) // 2
            # if mid is greater than right, then pivot is on right half
            if nums[mid] > nums[r]:
                l = mid + 1
            else: # pivot is on left side (can also be mid, so inclusive)
                r = mid

        # get element right after pivot
        pivot = l
        
        # depending on target, perform binary search on a half
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        result = binary_search(0, pivot - 1)

        if result != -1:
            return result
        
        return binary_search(pivot, len(nums) - 1)
        

        