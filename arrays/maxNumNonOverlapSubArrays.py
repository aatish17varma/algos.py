class Solution:
    
    def maxNonOverlapping(self, nums, target) -> int:
        hashMap = {0: -1} #totalSum -> inclusive ending index
        totalSum = 0
        answer = []
        count = 0
        for i in range(len(nums)):
            totalSum += nums[i]
            if totalSum - target in hashMap:
                answer.append([hashMap[totalSum-target] + 1, i])
            
            hashMap[totalSum] = i
        print(answer)
        ending = None
        for i in answer:
            if ending is None or i[0] > ending:
                count += 1
                ending = i[1]
        return count 
            
    def maxNonOverlapping(self, nums, target) -> int:
        prefixSum = {0: -1}
        count = 0
        endingIndex = None
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total-target in prefixSum and (prefixSum[total-target] + 1 > endingIndex or endingIndex is None):
                count += 1
                endingIndex = i 
            prefixSum[total] = i 
        return count
    
            
 
one = Solution()
#print(one.maxNonOverlapping([1,1,1,1,1],2))
#print(one.maxNonOverlapping([-1,3,5,1,4,2,-9], 6))
#print(one.maxNonOverlapping([-2,6,6,3,5,4,1,2,8], 10))
#print(one.maxNonOverlapping([0,0,0], 0))
print(one.maxNonOverlapping([2,1,1,-2,-3,-2,-2,1,3,1], 2))
