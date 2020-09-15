class Solution:
    def __init__(self):
        self.smallest = ""
    def smallestFromLeaf(self,root) -> str:
        helper(root, [])
        return self.smallest    


    def helper(self,root,string):
        if not root.left and not root.right:
            string.append(root.val)
            #convert num to string
            newString = []
            for i in range(len(string) -1, -1,-1):
                newString.append(chr(ord('a') - string[i])
            self.smallest = min(self.smallest, newString)

                   
        self.helper(root.left, string + [root.val])
        self.helper(root.right, string + [root.val])

