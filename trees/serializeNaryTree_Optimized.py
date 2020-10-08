# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Codec:
    def serialize(self, root: 'Node') -> str:
        if root is None:
            return ""
        def serializeHelper(root):
            childrenInformation = []
            for child in root.children:
                childrenInformation += (serializeHelper(child))
            return [chr(root.val), chr(len(root.children))] + childrenInformation
    
        serializedList = serializeHelper(root)
        print(serializedList)
        return "".join(serializedList)
    
    def deserialize(self, data: str) -> 'Node':
        if data == "":
            return None
        #global index
        global index
        index = 0
        def deserializeHelper(data):
            global index
            value = Node(ord(data[index]), [])
            index += 1
            for i in range(ord(data[index])):
                index += 1
                value.children.append(deserializeHelper(data))
            return value
        return deserializeHelper(data) 

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
tree = Node(1, [Node(3, [Node(5, []), Node(6,[])]), Node(2,[]), Node(4,[])])
one = Codec()
print("Before Serialized ")
print(tree)
serialized = (one.serialize(tree))
print(serialized)
deserialized = one.deserialize(serialized)
print("After Serialize / Deserialize ")
print(deserialized)
