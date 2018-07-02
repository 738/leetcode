class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        nodeList = self.inorder(root)
        counter, modes = collections.Counter(nodeList), []
        order = counter.most_common()
        maximum = order[0][1]
        for val in order:
            if val[1] == maximum: modes.append(val[0])
        return modes
        
    # if we traverse the BST in Inorder > we can get an sorted list of values
    def inorder(self, root):
        ans, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                ans.append(tmp.val)
                root = tmp.right
        return ans