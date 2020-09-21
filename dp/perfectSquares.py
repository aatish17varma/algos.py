'''
    Perfect Squares:
    - Given a positive integer n, return the least number of perfect squares that add up to n
    
    e.g. n=12 -> 3
         4 + 4 + 4 = 12

    DP Solution:
    if the problem T can be solved for all values i < n, then T(N) can be written as min(T(i) + t(N-i)) for all i. 

'''

from math import sqrt,floor 
class Solution:
    def numSquares(self, n: int) -> int: 
        dp = [0]
        for i in range(1, (n) + 1):
            if (sqrt(i) - floor(sqrt(i))) == 0:
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


    def perfectSquaresBFS(self, n) -> int:
        queue = [(n,0)]
        while len(queue) != 0:
            val = queue.pop(0)
            if val[0] == 0:
                return val[1]
            perfectSquares = []
            for i in range(1,val[0] + 1):
                if sqrt(i) - floor(sqrt(i)) == 0:
                    perfectSquares.append(i)
            for i in perfectSquares:
                if val[0] - i >= 0:
                    queue.append((val[0] - i, val[1] + 1))
       
one = Solution()
print(one.perfectSquaresBFS(14))
print(one.numSquares(14))


