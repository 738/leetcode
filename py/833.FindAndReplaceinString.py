class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        result = list(S)
        for i, index in enumerate(indexes):
            if S[index:index + len(sources[i])] == sources[i]:
                result[index] = targets[i]
                for j in range(1, len(sources[i])):
                    result[index + j] = ""
        return ''.join(result)
            

sol = Solution()
print(sol.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "fff"]))