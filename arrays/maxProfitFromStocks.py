def maxProfit(arr):
    beg = 0
    end = 1
    newBeg = None
    for i in range(2,len(arr)):
        print(beg,end,newBeg)
        if newBeg and arr[i] - arr[newBeg]  > arr[end] - arr[beg]:
            end = i
            beg = newBeg
            newBeg = None
        elif arr[i] > arr[end]:
            end = i 
        elif arr[i] < arr[beg]:
            if newBeg and arr[i] < arr[newBeg] or not newBeg:
                newBeg = i

    return (beg, end)

print(maxProfit([9, 11, 8, 5, 7, 10]))
        
