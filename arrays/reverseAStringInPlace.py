class Solution:
    def reverseString(self,arr):
        self.reverseFunction(arr, 0, len(arr) - 1)
        i = 0
        starting = 0 
        while i < len(arr):
            while i <= len(arr) - 1 and arr[i] != " ":
                i += 1
            self.reverseFunction(arr, starting, i-1) 
            i += 1
            starting = i

        return arr
    def reverseFunction(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

one = Solution()
print(one.reverseString(list("perfect makes practice")))

'''
    Time Complexity:
        n + n + w 
        w < n
        -> O(N) time complexity

    Space Complexity:
        O(1)
'''
            
