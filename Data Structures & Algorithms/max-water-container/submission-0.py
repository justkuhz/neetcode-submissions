'''
Problem domain is lists/arrays and pointers

Constraints:
How long is heights?
2 min to 1000 max

What is the range of values in heights?
0 to 1000

Can heights be empty?
No at least 2 elements

Approach and Complexity:
Two pointers from each edge, to keep we move whichever pointer is at a value smaller
than the other inwards and keep track of a running maximum
O(n) time and O(1) space
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # init two ptrs
        l = 0
        r = len(heights) - 1

        # running max
        most_water = 0

        # two pointer loop
        while l < r:
            # calculate area and update running max
            area = min(heights[l], heights[r]) * (r - l)
            most_water = max(most_water, area)

            # compare l and r, move smaller one inwards
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1 

        
        # return
        return most_water
        