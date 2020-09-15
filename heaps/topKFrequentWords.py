from heapq import heapify, heappop, heappush
class Solution:
    def topKFrequent(self, words, k): 
        answer = [] 
        hashMap = {}
        for i in words:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        heap = []
        heapify(heap)
        for key,val in hashMap.items():
            heappush(heap, (-val, key))
        counter = 0
        while counter < k:
            answer.append(heappop(heap)[1])
            counter += 1
        return answer




one = Solution()
print(one.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
