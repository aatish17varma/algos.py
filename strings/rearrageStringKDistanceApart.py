from heapq import heapify, heappush, heappop
class Solution:
    def rearrangeString(self, s, k) -> str:
        '''
            at any point, we want to insert the most frequent character who's last element is at least k value
            away. 

            if there are no elements that at are at least k values away, -> return ""

            if two elements have the same frequency x, and are at least k elements away, then it does not matter which element we keep first

        '''
        latestPositionOfNumber = {} #number -> latest position
        answer = []
        heap = []
        heapify(heap)
        elements = {}
        for i in range(len(s)):
            if s[i] not in elements:
                elements[s[i]] = 1
            else:
                elements[s[i]] += 1
        for key,value in elements.items(): heappush(heap, (-value, key))
        element = None
        while len(heap) != 0:
            heapLength = len(heap)
            element = heappop(heap)
            counter = 0
            store = []
            while (element[1]  in latestPositionOfNumber and len(answer) - latestPositionOfNumber[element[1]] < k):
                store.append(element)
                if len(heap) == 0:
                    return ""
                element = heappop(heap)
           
            for i in store:
                heappush(heap,i) 
            # we have a valid element
            answer.append(element[1])
            if element[0] < -1:
                heappush(heap, (element[0] + 1, element[1]))
            latestPositionOfNumber[element[1]] = 0 if len(answer) == 0 else len(answer) - 1
        return "".join(answer)

 
          
    

   


one = Solution()
print(one.rearrangeString("aabbcc", 3))
print(one.rearrangeString("aaabc", 3))
print(one.rearrangeString("aaadbbcc", 2))
