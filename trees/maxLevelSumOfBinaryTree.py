class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.levelsToSum = {}

    def maxLevelSum(self, root: TreeNode) -> int:
        self.helper(root, 1)
        maxSum = float("-inf")
        maxLevel = None
        for level, sums in root.items():
            if sums > maxSum:
                maxSum = sums
                maxLevel = level
        return maxLevel
        
     
    def helper(self, root, level):
        if root is None:
            return 
        if level not in self.levelsToSum:
            self.levelsToSum[level] = root.val
        else:
            self.levelsToSum[level] += root.val

        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)
        return
    
    
