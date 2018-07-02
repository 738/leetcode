class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root or (root.left is None and root.right is None): return False
        def inorder(root):
            stack, res = [], []
            while stack or root:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    tmpNode = stack.pop()
                    res.append(tmpNode.val)
                    root = tmpNode.right
            return res
            # if not root: return
            # inorder(root.left, list)
            # list.append(root.val)
            # inorder(root.right, list)
            
    
        nl = inorder(root)
        print(nl)
        s, e = 0, len(nl) - 1
        while True:
            if s >= e: break
            sum = nl[s] + nl[e]
            if sum < k: s += 1
            elif sum > k: e -= 1
            else: return True
        return False
        
        
        
        