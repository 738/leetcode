### Time Limit Exceeded 
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums, k, t):
#         for i, numi in enumerate(nums):
#             for j, numj in enumerate(nums[i + 1:]):
#                 if abs(numi - numj) <= t and j + 1 <= k:
#                     return True
#         return False

# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums, k, t):
#         if nums == []:
#             return False
#         result = list(enumerate(nums))
#         result.sort(key=lambda pair: pair[1])
#         previ, prevnum = result[0]
#         for i, num in result[1:]:
#             if abs(num - prevnum) <= t and abs(i - previ) <= k:
#                 return True
#             previ = i
#             prevnum = num
#         return False

from collections import OrderedDict
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False
        
        dic = OrderedDict()
        
        for i in range(len(nums)):
            key = nums[i]//max(1, t)
            for m in (key-t, key, key+t):
                if (m in dic) and abs(nums[i] - dic[m]) <= t:
                    return True
            
                dic[key] = nums[i]
            
                if i >= k:
                    dic.popitem(last = False)
            
        return False

sol = Solution()
print(sol.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))