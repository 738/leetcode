# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(root, acc):
            if not root: return acc
            acc = inorder(root.right, acc)
            root.val += acc
            acc = root.val
            acc = inorder(root.left, acc)
            return acc
        inorder(root, 0)
        return root
        