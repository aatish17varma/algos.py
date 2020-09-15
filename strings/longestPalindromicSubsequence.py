

store = {}


def longestPalindromicSubsequence(string):
    if string in store:
        return store[string]
    if len(string) == 0:
        store[""] = 0
        return 0
    if len(string) == 1:
        store[string] = 1
        return 1
    elif len(string) == 2:
        if string[0] == string[1]:
            store[string] = 2
            return 2
        else:
            store[string] = 1
            return 1
    answer = []
    for i in range(len(string)):
        firstCharacter = string[i]
        for j in range(len(string)-1,-1,-1):
            secondCharacter = string[j]
            if firstCharacter == secondCharacter:
                smallerAnswer = longestPalindromicSubsequence(string[i + 1 :  j])
                answer.append(smallerAnswer + 2 )
    store[string] = max(answer) if len(answer) > 0 else 1  
    return store[string]
print(longestPalindromicSubsequence("bbbab"))


