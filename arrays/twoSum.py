from random import randint
class Solution:
    def twoSum(self, nums,k) -> list:
        store = set()
        for i in range(len(nums)):
            if k - nums[i] in store:
                return [nums[i], k-nums[i]]
            store.add(nums[i])


one = Solution()
print(randint(0,3))
print(one.twoSum([4,7,1,-3,2],5))
