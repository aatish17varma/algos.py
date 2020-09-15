class Solution:
    def __init__(self):
        self.total = 0
    def sumNumbers(self, root: TreeNode) -> int:
        self.helper(root, [])    
        return self.total
    def helper(self, root, number):
        if not root.left and not root.right:
            self.total += int([root.val] + number)
        else:
            if root.left:
                self.helper(root.left, [root.val] + number) 
            if root.right:
                self.helper(root.right, [root.val] + number)

 
