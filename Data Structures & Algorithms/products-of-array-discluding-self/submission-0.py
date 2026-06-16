'''
Problem Domain:
Arrays / Lists, this problem tests our ability to process and evalute arrays with constraints on our operations.

Constraints:
- No division operation
Can we have an empty array? What should we return?
array will always have at least 2 elements

Can elements in our array be negative numbers?
yes, values range from -20 to 20

Are there any products that will exceed the 32 bit integer threshold?
no, guaranteed to fit in an integer

How long is nums array?
up to 1000 elements

Approach and Complexity:
- Key insight: at any point i in the array nums, to calculate the product of the array except self, we multiply the product of all elements to the left of i
with the product of all elements to the right of i
- We can create two arrays in O(n) time each, one for prefix (product of all elements to the left of i) and one for postfix (product of all elements to
the right of i)
- At any i position in our result / output array, we can multiple prefix[i] by postfix[i] to get the value of result[i]

Time complexity overall is O(n) (3 passes total) and space complexity is O(n) (3 additional arrays including output)

Post-problem thoughts:

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init arrays
        length = len(nums)
        prefix = [0] * length
        postfix = [0] * length

        # populate prefix
        product = 1
        prefix[0] = 1
        for i in range(1, length):
            product *= nums[i - 1]
            prefix[i] = product

        # populate postfix
        product = 1
        postfix[length - 1] = 1
        for i in range(length - 2, -1, -1):
            product *= nums[i + 1]
            postfix[i] = product

        # result list output
        return [x * y for x, y in zip(prefix, postfix)]
            
        
            