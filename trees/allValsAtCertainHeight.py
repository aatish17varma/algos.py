class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
    '''
    Approach 1:
    - traverse through the tree and when we reach a node at our goal height, add that node's value to our
    global array. We dont propogate downward because all child nodes will have a higher height than our goal. 
    
    Time Complexity: O(V), where V is the number of vertices
    Space Complexity: O(V). (In the worst case, the number of nodes == number of nodes at goal height, so we have to    store that). Also, because we are using recursion, our max stack value will be N if our tree is a line 

    '''
    answer = []  
    def helper(root, currentHeight, goalHeight):
        if root is None:
            return 
        if currentHeight == goalHeight:
            answer.append(root.value)
            return
        helper(root.left, currentHeight + 1, goalHeight)
        helper(root.right, currentHeight + 1, goalHeight)
 
    #helper(root, 1, height)
    '''
    Approach 2:
    Instead of adding an additional array

    This approach is slower than (1), because we will be constantly combining arrays, which does not occur in Approach 1. 
    '''
    def helperAlternative(root, currentHeight, goalHeight):
        if root is None:
            return []
        if currentHeight == goalHeight:
            return [root.value]
        leftVals = helperAlternative(root.left, currentHeight + 1, goalHeight)
        rightVals = helperAlternative(root.right, currentHeight + 1, goalHeight)
        return leftVals + rightVals

    return helperAlternative(root, 1 , height)


  # Fill this in.

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
# [4, 5, 7]
