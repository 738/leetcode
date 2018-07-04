import sys
sys.setrecursionlimit(100000)

def findMaxNode(node):
        while node.right:
            node = node.right
        return node.val

class Solution:
    def deleteNode(self, root, key):
        if not root: return None
        if root.val == key:
            if not root.left and not root.right: return None
            elif not root.left: return root.right
            elif not root.right: return root.left
            else:
                root.val = findMaxNode(root.left)
                root.left = self.deleteNode(root, root.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root