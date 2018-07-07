# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root: return 0
            l, r = 0, 0
            if root.left:
                l = dfs(root.left)
                l = l + 1 if root.left.val == root.val else 0
            if root.right:
                r = dfs(root.right)
                r = r + 1 if root.right.val == root.val else 0
            self.res = max(self.res, l + r)
            return max(l, r)
        
        if not root: return 0
        dfs(root)
        return self.res
