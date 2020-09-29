class LinkedList:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
class Solution:
    def intersection(self,l1,l2):
        vals = set()
        i = l1
        while i is not None:
            vals.add(i)
            i = i.next
        j = l2
        while j is not None:
            if j in vals:
                return j.val
            j = j.next
        return None

'''
    
    LinkedLists Looks Like:

    1 -> 5
         -> 3 -> 4
    7 -> 8

'''

one = Solution()
intersection = LinkedList(2,LinkedList(3,LinkedList(4)))
first = LinkedList(1, LinkedList(5, intersection))
second = LinkedList(7, LinkedList(8, intersection))
print(one.intersection(first,second))
