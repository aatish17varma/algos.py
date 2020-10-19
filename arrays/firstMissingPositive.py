'''
You are given an array of integers. Return the smallest positive integer that is not present in the array. The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist in the array.
'''

'''
    Time = O(nlogn)
    Space = O(1)
'''
def findMissingPositive(arr):
    if len(arr) == 0:
        return 1
    arr.sort()
    lastNumber = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            continue
        else:
            if arr[i] == lastNumber + 1:
                lastNumber = arr[i]
            else:
                return lastNumber + 1
    return lastNumber + 1

print(findMissingPositive([3, 4, -1, 1]))

'''
    Time = O(N)
    Space = O(1)
'''

def findMissingPositiveFaster(arr):
    beg = 0
    end = len(arr) - 1
    while beg <= end:
        while arr[beg] > 0:
            beg += 1 
        while arr[end] <= 0:
            end -= 1
        if beg <= end:
            arr[beg], arr[end] = arr[end], arr[beg]
            beg += 1
            end -= 1
    for i in range(0, beg):
        if abs(arr[i]) - 1 <= (beg - 1):
            arr[abs(arr[i]) - 1] *= -1 
    for i in range(0, beg):
        if arr[i] > 0:
            return i + 1
    return beg

'''
    Time = O(N)
    Space = O(N)
'''
def findMissingPositiveMedium(arr):
    arrSet = set(arr)
    for i in range(1, len(arr) + 1):
        if i not in arrSet:
            return i


print(findMissingPositiveFaster([3,4,-1,1]))
print(findMissingPositiveMedium([3,4,-1,1]))


