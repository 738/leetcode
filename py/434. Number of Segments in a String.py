class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # # my sol1
        # sum = 0
        # for str in s.split(" "):
        #     if str != "": sum+=1
        # return sum

        # my sol2
        return sum([t != "" for t in s.split(" ")])

        # solution
        # return len(s.split())