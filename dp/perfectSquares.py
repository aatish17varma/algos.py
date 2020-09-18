'''
    Perfect Squares:
    - Given a positive integer n, return the least number of perfect squares that add up to n
    
    e.g. n=12 -> 3
         4 + 4 + 4 = 12

    DP Solution:
    if the problem T can be solved for all values i < n, then T(N) can be written as min(T(i) + t(N-i)) for all i. 

'''

import math
class Solution:
    def numSquares(self, n: int) -> int: 
        dp = [0]
        for i in range(1, (n) + 1):
            if (math.sqrt(i) - math.floor(math.sqrt(i))) == 0:
                dp.append(1)
            else: 
                beg = 1 
                end = len(dp) - 1
                minAnswer = float('inf')
                while beg <= end:
                    minAnswer = min(minAnswer,dp[beg] + dp[end])
                    beg += 1
                    end -= 1
                dp.append(minAnswer)
        return dp[-1] 

one = Solution()
print(one.numSquares(12)) 
print(one.numSquares(13))
print(one.numSquares(14))


