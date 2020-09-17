class Solution:
    def decodeString(self, s) -> str:
        stack = []
        currentString = []
        newString = []
        numbers = []
        number = []
        string = []
        for i in range(len(s)):
            stack.append(s[-1])
            if s[i] == "[":
                numbers.append("".join(number))
                number = []
                currentString= []
            elif s[i] == "]":
                string.append("".join(currentString))
                currentString = [] 
                number = []
                #pop all characters from stack that form the newString
                i = 0
                while i < len(numbers[-1]) + 2 + len(string[-1]):
                    stack.pop(-1)
                    i += 1
                # create the new string 
                newString = [string[-1] for _ in range(int(numbers[-1]))]
                string.pop(-1)
                numbers.pop(-1)
                stack.append("".join(newString))
            else:
                if not s[i].isdigit():
                    currentString.append(s[i])
                if s[i].isdigit():
                    number.append(s[i])
        
        return "".join(stack)
    
one = Solution()
print(one.decodeString("3[a]2[bc]")) 
print(one.decodeString("3[a2[c]]"))
