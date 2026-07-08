'''
problem domain: lists, stacks

constraints:
1) can tokens be empty?
no
2) is tokens ever invalid / can we be left with one integer and one operand and how to handle?
never invalid

approach and complexity:
we can solve this in one pass O(n) by using a stack and sequentially processing an operator
and the previous two stack elements until we fully process tokens list. Then we return top of
stack (last element)
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init stack
        stack = []

        # iterate over tokens list
        for t in tokens:
            # check if num or operator
            if t not in ["+", "/", "-", "*"]:
                stack.append(int(t))

            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if t == "+":
                    stack.append(num1 + num2)
                    
                elif t == "-":
                    stack.append(num1 - num2)

                elif t == "*":
                    stack.append(num1 * num2)

                else: # t == "/"
                    stack.append(int(num1 / num2))


        return stack[0]