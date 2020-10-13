from heapq import heappop, heappush,heapify
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
    listToReturn = Node(None,None)
    pointer = listToReturn
    heap = [(i.val, i) for i in lists]
    heapify(heap)
    while len(heap) > 0:
        valPopped = heappop(heap)
        listToReturn.next = Node(valPopped[0])
        listToReturn = listToReturn.next
        if valPopped[1].next:
            heappush(heap, (valPopped[1].next.val, valPopped[1].next))
    return pointer.next


def mergeImproved(lists):
    def merge(l1,l2):
        first = 0
        second = 0
        answer = []
        while first < len(l1) and second < len(l2):
            if l1[first] < l2[second]:
                answer.append(l1[first])
                first += 1
            elif l1[first] > l2[second]:
                answer.append(l2[second])
                second += 1
        if first < len(l1):
            answer += l1[first : ]
        elif second < len(l2):
            answer += l2[second : ]
        return answer

    if len(lists) == 2:
        return merge(lists[0], lists[1])

    first = mergeImproved(lists[0 : len(lists) // 2])
    second = mergeImproved(lists[len(lists) // 2 : ])
    return merge(first,second)


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
a1 = [1,3,5]
a2 = [2,4,6]
print(mergeImproved([a1,a2]))
# 123456
