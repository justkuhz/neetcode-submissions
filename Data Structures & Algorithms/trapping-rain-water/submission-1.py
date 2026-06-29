'''
Problem domain: Lists/Pointers

Constraints:
How do we consider the edges of the array for height? Is it 0?
Yes it is 0

Can numbers in heights be negative or min 0?
No, min is 0

How large can values in heights be?
Up to 1000

How many numbers in heights? Can it be empty?
Guaranteed at least 1 up to 1000

Key Insight:
At any index i, the amount of water trapped is min(max_left, max_right) - height[i] where it
cannot be below 0.

1) We can fill out two arrays for the max_left and max_right at any given index and use that
to calculate a running sum which gives us the maximum area of water trapped between bars
O(n) time and O(n) space

2) We can use two pointers and increment them inwards based off of which ptr is smaller
O(n) time and O(n) space
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # init pointers and res
        res = 0
        l = 0
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]

        # move ptrs
        while l < r:
            # compare ptrs to determine which to shift
            if max_left <= max_right:
                # shift pointer
                l += 1

                # calculate water at current index and add to res
                water = min(max_left, max_right) - height[l]
                if water > 0:
                    res += water

                # check if there is a new max_left
                max_left = max(max_left, height[l])
            else:
                # shift pointer
                r -= 1
                
                # calculate water at current index and add to res
                water = min(max_left, max_right) - height[r]
                if water > 0:
                    res += water
                
                # check if there is a new max_right
                max_right = max(max_right, height[r])
            
        # return res
        return res
        