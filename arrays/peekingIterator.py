# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peekedValue = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peekedValue:
            return self.peekedValue
        else:
            self.peekedValue = self.iterator.next()
        return self.peekedValue
        
    def next(self):
        """
        :rtype: int
        """
        if self.peekedValue:
            oldVal = self.peekedValue
            self.peekedValue = None
            return oldVal
        else: # we have not moved the iterator yet
            return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peekedValue: # if the next value is a number (not None or False), then we have a next value 
            return self.peekedValue
        if self.peekedValue == False: # False indicates we haven't called the peak() and we are not 1 ahead of the iteratork
            self.iterator.hasNext()
        else: # reaching here means that self.peekedValue == None, meaning that the next value is None, therefore we dont have a next
            return False

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
