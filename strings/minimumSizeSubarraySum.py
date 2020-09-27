class Solution:
    def minSize(self, arr, target):
        total = 0
        seen = dict()
        minAnswer = float('inf')
        for i in range(len(arr)):
            total += arr[i]
            if total - target in seen:
                minAnswer = min(minAnswer,i - seen[total-target])
            seen[total] = i 

        return minAnswer if minAnswer != float('inf') else 0


'''
    Time Complexity: O(N)
    Space Complexity: O(N)
'''

one = Solution()
print(one.minSize([2,3,1,2,4,3], 7))
