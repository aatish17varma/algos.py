class maxStack:
    def __init__(self):
        self.stack = []
        self.maxVal = None

    def push(self,val):
        value = {"value" : val, "oldMax": self.maxVal} 
        if self.maxVal is None:
            self.maxVal = val
        else:
            self.maxVal = max(self.maxVal, val)
        self.stack.append(value)
        return 

    def pop(self):
        if len(self.stack) == 0:
            return
        value = self.stack.pop(-1)
        if value["value"] == self.maxVal:
            self.maxVal = value["oldMax"]
        return
        
    def max(self):
        return self.maxVal

one = maxStack()
one.push(1)
one.push(2)
one.push(3)
one.push(2)
print(one.max())
one.pop()
one.pop()
print(one.max())


