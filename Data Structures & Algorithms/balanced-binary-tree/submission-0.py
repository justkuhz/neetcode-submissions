# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
brute force wastes a lot of time by repeatedly recomputing subtree heights we've already seen

we can use one DFS that returns two things at once for every node:
1) is subtree balanced?
2) what is its height

this way each subtree is only processed once and at any node where the height difference > 1 we can mark it as unbalanced and early exit

dfs function should return [isBalanaced (bool), height (int)]
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            # base case
            if not root:
                return [True, 0]

            # call dfs on children
            left, right = dfs(root.left), dfs(root.right)

            # check to see its balanced
            # both children are balanced and height diff is <= 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # return
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
