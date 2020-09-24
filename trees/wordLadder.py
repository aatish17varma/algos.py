class Solution:
        def ladderLength(self, beginWord, endWord, wordList) -> int:

            def difference(beginWord, endWord):
                if len(beginWord) != len(endWord):
                    return False 

                count = 0
                for i in range(len(beginWord)): 
                    if beginWord[i] != endWord[i]:
                        if count == 1:
                            return False
                        count += 1 
                
                return True

            if endWord not in wordList:
                return 0

            queueBegin = [beginWord]
            queueEnd = [endWord]
            hashMapBegin = {beginWord : 1}
            hashMapEnd = {endWord : 0}
            while len(queueBegin) > 0 and len(queueEnd) > 0:
                val = queueBegin.pop(0)
                if val in hashMapEnd:
                    return hashMapBegin[val] + hashMapEnd[val] 

                for i in wordList:
                    if difference(i,val) and i not in hashMapBegin:
                        queueBegin.append(i)
                        hashMapBegin[i] = hashMapBegin[val] + 1
                
                endVal = queueEnd.pop(0)
                if endVal in hashMapBegin:
                    return hashMapBegin[endVal] + hashMapEnd[endVal] 
                for i in wordList:
                    if difference(i,endVal) and i not in hashMapEnd:
                        queueEnd.append(i)
                        hashMapEnd[i] = hashMapEnd[endVal] + 1

            return 0


one = Solution()
print(one.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(one.ladderLength("hit","cog",["hot","dot","dog","lot","log"]))

