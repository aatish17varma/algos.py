class Solution:
    def twoSum(self, nums,k) -> list:
        store = {}
        for i in range(len(nums)):
            if k - nums[i] in store:
                return [nums[i], k-nums[i]]
            store[nums[i]] = True

one = Solution()
print(one.twoSum([4,7,1,-3,2],5))
