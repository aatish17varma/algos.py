import random
#def quickSelect(arr, k):

def helper(arr, k, pivot, right):
    while True:
        left = pivot + 1
        while left < right:
            if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
                arr[left], arr[right] = arr[right], arr[left]
            if arr[left] <= arr[pivot]:
                left +=1 
            if arr[right] >= arr[pivot]:
                right -= 1

        arr[pivot], arr[right] = arr[right], arr[pivot]
        
        if right == k - 1:
            return arr[right]
        else:
            if right > k-1:
                pivot = 0
                right = k-2
            else: #if right < k-1
                pivot = k  
    return None
print(helper([3, 5, 2, 4, 6, 8],4,0,5))
