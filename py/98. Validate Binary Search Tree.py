# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# easy solution
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        nums = inorder(root)
        # 정렬이 잘되어있는지 체크
        for i in range(0, len(nums) - 1):
            if nums[i] >= nums[i + 1]: return False
        return True

# # another solution
# class Solution:
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         def inorder(root, num, ans):
#             if not root: return num
#             num = inorder(root.left, num)
#             if num >= root.val: a=False
#             num = root.val
#             num = inorder(root.right, num)
#             return num
#         inorder(root, 0)
#         return a


# def inorder(root):
#     if not root: return []
#     list = []
#     list.extend(inorder(root.left))
#     list.append(root.val)
#     list.extend(inorder(root.right))
#     return list