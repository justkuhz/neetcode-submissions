# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Diameter of a binary tree is the longest path between any two nodes, this path must go through some node and at that node the path length is:
left subtree height + right subtree height

we can perform DFS to compute heighs and simultaneously track the maximum left + right seen so far so we don't have to recompute heights we've already calculated

O(n) time O(n) space
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root) -> int:
            # allow us to reference res
            nonlocal res

            # base case
            if not root:
                return 0

            # recurse left and right
            left = dfs(root.left)
            right = dfs(root.right)
            
            # update res with max seen so far
            res = max(res, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return res