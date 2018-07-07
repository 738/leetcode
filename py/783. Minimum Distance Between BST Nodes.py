# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        nums = inorder(root)
        res = []
        for num1, num2 in zip(nums, nums[1:]):
            res.append(num2 - num1)
        return min(res)