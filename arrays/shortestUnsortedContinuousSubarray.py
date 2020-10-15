class Solution:
    def findUnsortedSubarray(self, nums): 
        stack = []
        left, right = len(nums) - 1, 0
        for i in range(len(nums)):
            if i == 0:
                stack.append(i)
            else:
                while nums[stack[-1]] > nums[-1]:
                    left = min(left, stack.pop(-1))
                stack.append(i)
        return left
                

