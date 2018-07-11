class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return any([A[i:len(A)] + A[0:i] == B for i in range(len(A))]) if A or B else True