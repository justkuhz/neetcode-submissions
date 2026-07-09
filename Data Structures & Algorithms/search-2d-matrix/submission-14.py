'''
perform binary search vertically to find correct row, and then binary search again to find 
correct column

we know its correct row to search if mid is less than target and next row starts with number
greater than target
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        lo = 0
        hi = len(matrix) - 1
        row = -1

        while lo < hi:
            mid = lo + (hi - lo + 1) // 2

            if matrix[mid][0] <= target:
                lo = mid
            else:
                hi = mid - 1

        row = lo

        # find column
        lo = 0
        hi = len(matrix[row]) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if matrix[row][mid] > target:
                hi = mid - 1
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                return True

        return False
        