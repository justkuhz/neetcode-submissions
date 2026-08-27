# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
at each node we want to swap the right and left pointers
we can recurse down dfs in order N L R and do this in one pass
O(n) time and O(1) extra space
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        def dfs(node):
            # base case
            if not node:
                return
            
            if node.left and node.right:
                node.right, node.left = node.left, node.right
                dfs(node.right)
                dfs(node.left)
            elif node.left:
                node.right = node.left
                node.left = None
                dfs(node.right)
            elif node.right:
                node.left = node.right
                node.right = None
                dfs(node.left)
        
        dfs(root)
        return root

        