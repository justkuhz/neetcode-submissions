'''
problem domain: stacks, lists

approach and complexity:
we can use a stack to hold onto days that are still waiting for a warmer day to appear
before we can fill out their respective outputs
one pass O(n) time O(n) space
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create res list with 0's, init stack
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        # iterate over temperatures
        for i, t in enumerate(temperatures):
            # check if temp is warmer than top of stack
            while stack and t > stack[-1][0]:
                # if it is, we pop and update result
                prev_temp, prev_index = stack.pop()
                res[prev_index] = i - prev_index                
            
            stack.append((t, i))

        return res
            

        