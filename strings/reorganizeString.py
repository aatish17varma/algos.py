from heapq import heapify, heappush, heappop
class Solution:
    def reorganizeString(self, string):
        answer = []
        hashMap = {}
        for i in string:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        heap = [(-value,key) for key,value in hashMap.items()]
        heapify(heap)
        print(heap)
        while len(heap) != 0:
            first = heappop(heap)
            second = heappop(heap) if len(heap) > 0 else None
            if len(answer) > 0:
                if answer[-1] != first[1]:
                    answer.append(first[1])
                    if second:
                        heappush(heap, second)
                    if first[0] < -1:
                        heappush(heap, (first[0] +  1, first[1]))
                elif second and answer[-1] != second[1]:
                    answer.append(second[1])
                    heappush(heap,first)
                    if second[0] < -1:
                        heappush(heap,(second[0] +  1, second[1]))
                else:
                    return ""
            else:
                answer.append(first[1])
                if first[0] < -1:
                    heappush(heap,(first[0] +  1, first[1]))
                if second:
                    heappush(heap,second)
            
        return "".join(answer)

one = Solution()
print(one.reorganizeString("aab"))
print(one.reorganizeString("aaab"))
print(one.reorganizeString("vvvlo"))
print(one.reorganizeString("zhmyo"))
