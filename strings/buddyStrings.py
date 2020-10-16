class Solution:
    def buddyStrings(self, A, B) -> bool:
        if len(A) != len(B):
            return False

        seenPairs = set() 
        samePairs = 0 #we've arrived at (1,1) and (1,1) is in our seenPairs set
        swapPairs = 0  # we've arrived at (1,2) and (2,1) is in our seenPairs set
        differentPairs = 0

        for i in range(len(A)):
            pair = (A[i], B[i])
            if pair[1] != pair[0]:
                differentPairs += 1

            if (pair[1], pair[0]) in seenPairs:
                if pair[0] == pair[1]: 
                    samePairs += 1
                else:
                    swapPairs += 1
            else:
                seenPairs.add(pair)


        if differentPairs == 0:
            return samePairs >= 1
        elif differentPairs == 2: 
            return samePairs == 1

        return False


one = Solution()
print(one.buddyStrings("ab", "ab"))
