class LinkedList:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
class Solution:
    #O(N) time and O(N) space
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


    # O(N) time and O(1) space. 
    '''
        if l1 = x + s
           l2 = y + s
        if we continue to walk 1 step at at a time in each linkedlist, and hten
        switch to the other, eventually we would have walked 

        x + s + y and y + s + x, both of which point to the start of the cycle

    '''
    def intersectionOptimized(self,l1,l2):
        first = l1
        second = l2
        while first is not second:
            if first.next:
                first = first.next
            else:
                first = l2
    
            if second.next:
                second = second.next
            else:
                second = l1
        return first.val or second.val
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
print(one.intersectionOptimized(first,second))
