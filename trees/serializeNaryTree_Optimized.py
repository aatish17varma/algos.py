# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    '''
        Time Complexity : O(V + E)
        Space Complexity : O(V)
    '''
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
    '''
        Time Complexity : O(N) - we are doing a lot of recursion, but it still comes to 1 pass over the input string 
        Space Complexity : O(V) - We are making a new tree with V nodes and E edges. E < V, so complexity = O(V). Also we are using recursion, and in the worst case, the space taken
        up by the call stack is O(V). So overall complexity = V + V = O(V)
    ''' 
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
