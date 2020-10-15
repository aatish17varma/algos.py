class Node:
    def __init__(self,value,children=[]):
        self.value = value
        self.children = children

class Codec:
    def serialize(self, root):
        def helper(root):
            allChildren = ["["]
            for child in root.children:
                childNode = helper(child)
                allChildren.append(childNode)
                allChildren.append(",")
            if len(allChildren) >= 2:
                allChildren.pop(-1)
            allChildren.append("]")
            allChildren = "".join(allChildren)
            return "[" + str(root.value) + "_" + allChildren + "]"
        return helper(root)

    def deserialize(self, data):
        def helper(data):
            if data == "[]":
                return None
            value = data[1 : data.index("_")]
            listOfChildren = data[data.index("_") + 1 : len(data) - 1] # [ [] , [] , [] ,]
            #find all children using a stack and a while loop
            stack = ["["]
            i = 2
            allChildren = []
            currentChild = ["["]
            while i < len(listOfChildren) - 1:
                while len(stack) != 0:
                    if listOfChildren[i] == "[":
                        stack.append("[")
                    elif listOfChildren[i] == "]":
                        if len(stack) > 0:
                            stack.pop(-1)
                    currentChild.append(listOfChildren[i])
                    i += 1
                allChildren.append("".join(currentChild))
                currentChild = ["["]
                i += 2
                stack = ["["]

            kidNodes = []
            for child in allChildren:
                kidNodes.append(helper(child))
            newNode = Node(int(value), kidNodes)
            return newNode


        return helper(data)
'''
    Time Complexity:
        Serialize = O(V + E)

    Space Complexity:
        Serialize = 




'''

tree = Node(1, [Node(3, [Node(5, []), Node(6,[])]), Node(2,[]), Node(4,[])])
one = Codec()
print("Before Serialized ")
print(tree)
serialized = (one.serialize(tree))
deserialized = one.deserialize(serialized)
print("After Serialize / Deserialize ")
print(deserialized)
