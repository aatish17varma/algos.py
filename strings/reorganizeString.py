from heapq import heappush, heapify, heappop
def reorganizeString(string: str) -> str:
    hashMap = {} 
    for i in range(len(string)):
        hashMap[string[i]] = 1 if string[i] not in hashMap else hashMap[string[i]] + 1 
    heap = [(-value,key) for key,value in hashMap.items()]
    heapify(heap)
    answerArray = [] 
    while len(heap) != 0:
        
        firstItem = heappop(heap)
        secondItem = None
        if len(heap) >= 1:
            secondItem = heappop(heap)

        if len(answerArray) == 0:
            answerArray.append(firstItem[1])
            heappush(heap, (firstItem[0] - 1, firstItem[1]))
            if secondItem is not None:
                heappush(heap, secondItem)

        elif answerArray[-1]  == firstItem[1]:
            if secondItem:
                answerArray.append(secondItem[1])
                if secondItem[0] + 1 != 0:
                    heappush(heap, (secondItem[0] - 1, secondItem[1]))
                heappush(heap, firstItem)
            else:
                return ""
        elif answerArray[-1] == secondItem[1]:
            answerArray.append(firstItem[1])
            if firstItem[0] + 1 != 0:
                heappush(heap, (firstItem[0] - 1, firstItem[1]))
            heappush(heap, secondItem) 
        else:
            return ""



    return "".join(answerArray)
print(reorganizeString("aab"))
print(reorganizeString("aaab"))

 
