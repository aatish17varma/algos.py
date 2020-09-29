import randint from random
class Solution:
    def quickSelect(self,arr,n):
        rand = randint(0, n)
        i = 0 
        j = len(arr) - 1
        while True:
            while i < j:
                while arr[i] <= arr[rand]: 
                    i += 1
                while arr[j] > arr[rand]:
                    j -= 1 
                arr[i], arr[j] = arr[j], arr[i] 
         
