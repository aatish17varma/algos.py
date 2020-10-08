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
            listOfChildren = data[data.index("_") + 1 : len(data) - 1]
            listOfChildren = listOfChildren.split(",")
            childNodes = []
            for child in listOfChildren:
                print(child)
                childNodes.append(helper(child))
            newNode = Node(int(value), childNodes)
            return newNode
        return helper(data)

tree = Node(1, [Node(3, [Node(5, []), Node(6,[])]), Node(2,[]), Node(4,[])])
one = Codec()
serialized = (one.serialize(tree))
print(serialized)
deserialized = one.deserialize(serialized)
print(deserialized)
