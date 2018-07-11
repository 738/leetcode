class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.top() == None: return
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0: return None
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        min = float("inf")
        for num in self.stack:
            if num < min: min = num
        return min
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()