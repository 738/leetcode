class Solution:
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())
        # return any([word.isupper(), word.islower(), all([word[0].isupper(), word[1:].islower()])])

sol = Solution()
print(sol.detectCapitalUse("USA"))
print(sol.detectCapitalUse("FlaG"))
print(sol.detectCapitalUse("G"))