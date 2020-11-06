class Solution:
    def productOfArray(self, arr):
        l, r, a = [],[],[]
        for i in range(len(arr)):
            if i == 0:
                l.append(1)
            else:
                l.append(arr[i-1] * l[-1])
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                r.append(1)
            else:
                r.append(arr[i + 1] * r[-1])
        
        return [l[i] * r[len(arr) - 1 - i] for i in range(len(arr))]


print(Solution().productOfArray([1,2,3,4]))


        
