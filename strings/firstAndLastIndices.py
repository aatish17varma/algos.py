def firstAndLastIndicesElement(arr, num):
    firstIndex = None
    for i in range(len(arr)):
        if arr[i] == num:
            firstIndex = i
            break
    if firstIndex is None:
        return [-1,-1]
    
    
    for i in range(firstIndex + 1, len(arr)):
        if arr[i] != num:
            return [firstIndex, i - 1]
    

    return [firstIndex, len(arr) - 1] 


print(firstAndLastIndicesElement([100,150,150,153], 150))
print(firstAndLastIndicesElement([1,3,3,5,7,8,9,9,9,15], 9))
print(firstAndLastIndicesElement([1,2,3,4,5,6,10], 9))
