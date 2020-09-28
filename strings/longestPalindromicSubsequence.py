class Solution:
    def __init__(self):
        self.store = {}
    def longestPalindromicSubsequence(self,string):
        if string in self.store:
            return self.store[string]
        if len(string) == 0:
            self.store[""] = 0
            return 0
        if len(string) == 1:
            self.store[string] = 1
            return 1
        elif len(string) == 2:
            if string[0] == string[1]:
                self.store[string] = 2
                return 2
            else:
                self.store[string] = 1
                return 1
        answer = []
        for i in range(len(string)):
            firstCharacter = string[i]
            for j in range(len(string)-1,-1,-1):
                secondCharacter = string[j]
                if firstCharacter == secondCharacter:
                    smallerAnswer = self.longestPalindromicSubsequence(string[i + 1 :  j])
                    answer.append(smallerAnswer + 2 )
        self.store[string] = max(answer) if len(answer) > 0 else 1  
        return self.store[string]


one = Solution()
print(one.longestPalindromicSubsequence("bbbab"))


