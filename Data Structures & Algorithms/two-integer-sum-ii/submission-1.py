'''
Problem domain: arrays/lists, sorting, two pointers

Constraints:
Is there a real solution or how should we handle returning not found?
one real solution
What is the range of integers that can be found in the list numbers?
-1000 to 1000
How long can the list numbers be?
at least 2, up to 1000

Approach and complexity:
The key insight to this problem is that the array is sorted. This means we can use two pointers
and decrement/increment either one depending on how their sum compares to the target. This 
method allows us to solve it in O(n) time worst case we check each element in numbers list once.
O(1) space as we only need to keep track of two pointer indexes.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # init pointers
        l = 0
        r = len(numbers) - 1

        # loop
        while l < r:
            # check if we should break and return
            cur = numbers[l] + numbers[r]
            if cur == target:
                return [l + 1, r + 1]
            
            if cur > target:
                r -= 1
            else:
                l += 1
        
        
        