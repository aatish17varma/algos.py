class Solution:
    #O(N) time, O(1) space
    def searchRange(self, nums, target):
        left = right = -1
        for i in range(len(nums)):
            if nums[i] == target:
                left = i
                break

        for j in range(len(nums) -1, -1,-1):
            if nums[j] == target:
                right = j
                break

        return [left,right]

    def searchRangeFast(self,nums,target):
        def findPosition(beg, end, findLeft):
            val = -1
            while beg < end: 
                mid = (beg + end) // 2
                if nums[mid] < target:
                    beg = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    val = mid
                    if findLeft:
                        end = mid - 1
                    else:
                        beg = mid + 1
            #if target is not in array, either (1) beg == end and nums[beg] != target or (2) beg > end
            if beg == end and nums[beg] == nums[end] == target:
                val = beg
            return val

        left = findPosition(0,len(nums)-1,True)
        right = findPosition(0,len(nums)-1, False)
        return [left,right]
      
        
        
one = Solution()
print(one.searchRangeFast([5,7,7,8,8,10],8))
print(one.searchRangeFast([5,7,7,8,8,10],6))
print(one.searchRangeFast([2,2],1))
