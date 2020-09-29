from math import pow, sqrt
#O(n^2) solution
class Solution:
    def triplets(self, arr):
        hashMap = {}
        for i in arr:
            hashMap[i] = True
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if sqrt(pow(arr[i],2) + pow(arr[j],2)) in hashMap:
                    return True
        return False
one = Solution()
print(one.triplets([3,5,12,5,13]))

