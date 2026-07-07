'''
problem domain: string, list/arrays, stacks, LIFO

approach and complexity:
we can use a stack and match closing brackets to open brackets
we can also use a map to reduce the code complexity and optimize checking matching open
close branckets
Time O(n), space O(n)

Key insight:
Why is using a stack here really good?

What does using a map help optimize?
'''
class Solution:
    def isValid(self, s: str) -> bool:
        # easy edge case, valid parenth must be even
        if len(s) % 2 == 1:
            return False

        stack = []
        p_map = {"{":"}", "[":"]", "(":")"}

        # iterate over string s
        for p in s:
            # if open parenth, we push into stack
            if p in p_map.keys():
                stack.append(p)
            # if closing parenth, we try to match
            else:
                # 1) no open parentheses
                if not stack:
                    return False
                
                # pop stack
                last = stack.pop()

                # 2) mismatch in parentheses
                if p_map[last] != p:
                    return False

        return not stack
            

        
        