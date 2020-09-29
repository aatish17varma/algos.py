class LinkedList:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

    def findNode(self,val):
        current = self
        while current.val is not val:
            current = current.next
        return current

    def tail(self):
        current = self
        while current.next is not None:
            current = current.next
        return current


