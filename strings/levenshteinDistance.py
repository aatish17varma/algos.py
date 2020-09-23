'''
    Levenshtein Distance:
    given two strings s1 and s2, find the least number of transformations that can be done to one string to transform it in to the other

    a transformation is decribed as adding a character, removing a character, and replacing a character with a different one

'''
class Solution:
    '''
        Dynamic Programming:
            if the last character of the two strings is the same, then the answer is the answer of the subproblem where the last character of broth strings are excluded
            if the last characters are different, then the answer to the problem is the minimum of the three subproblems where the last character of s1 is elided, the last character of s2 is elided, and the last character of both strings are elided

            base case is s1 = "" and s2 != "", then answer = len(s2)
                         s2 != "" and s1 == "", answer = len(s1)
    '''
    def distance(self,s1,s2) -> int:
        dp = [[None if i != 0 else 0  for i  in range(len(s1) + 1)] for _ in range(len(s2) +  1)]
        for i in range(1, len(dp)):
            dp[i][0] = dp[i-1][0] + 1
        for j in range(1,len(dp[0])):
            dp[0][j] = dp[0][j-1] + 1
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if s2[i-1] == s1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 1, dp[i-1][j] + 1, dp[i][j-1] + 1)
        print(dp)
        return dp[-1][-1]

one = Solution()
print(one.distance("biting", "sitting")) 
print(one.distance("insert", "desert"))
print(one.distance("yo","computer"))
