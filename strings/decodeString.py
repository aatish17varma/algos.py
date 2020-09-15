class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        frequencies = []
        strings = []
        string = []
        frequency = []
        openingBrackets = []
        for i in range(len(s)):
            if s[i] == "[":
                frequencies.append("".join(frequency))
                frequency = []
                openingBrackets.append(i)
                stack.append(s[i])
            elif s[i] == "]":
                strings.append(string)
                string = []
                for i in range(int(frequencies[-1])):
                    stack.append(strings[-1])
            else:
                string.append(s[i])
                
                
                 
            
one = Solution()
print(one.decodeString("3[a]2[bc]"))
