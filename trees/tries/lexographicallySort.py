'''
Given a list of words sort them lexicographically
'''
dict = [
        "lexicographic", "sorting", "of", "a", "set", "of", "keys", "can", "be",
        "accomplished", "with", "a", "simple", "trie", "based", "algorithm",
        "we", "insert", "all", "keys", "in", "a", "trie", "output", "all",
        "keys", "in", "the", "trie", "by", "means", "of", "preorder",
        "traversal", "which", "results", "in", "output", "that", "is", "in",
        "lexicographically", "increasing"]
 
class Node:
    def __init__(self):
        self.arr = [None for _ in range(27)]

def formTrie(allWords):
    trie = Node()

    def fromTrieFromWord(trie, word):
        if len(word) == 0:
            trie.arr[-1] = Node()        
        
        elif trie.arr[ord(word[0]) - ord('a')] is not None:
            fromTrieFromWord(trie.arr[ord(word[0]) - ord('a')], word[1 : ])
        else:
            trie.arr[ord(word[0]) - ord('a')] = Node()
            fromTrieFromWord(trie.arr[ord(word[0]) - ord('a')], word[1 : ])   
    
    for word in allWords:
        fromTrieFromWord(trie, word)

    return trie 


trie = formTrie(dict)
def dfs(trie):
    answer = []
    def helper(trie, word):
        if len(trie.arr) == 0:
            answer.append(word)
            return
        for eachNodeIndex in range(len(trie.arr)):
            if trie.arr[eachNodeIndex] is not None:
                    if eachNodeIndex == 26:
                        answer.append("".join(word))
                    else:
                        helper(trie.arr[eachNodeIndex], word + [(chr(eachNodeIndex + ord('a')))])
        return

    helper(trie, [])
    return answer

print(dfs(trie))

