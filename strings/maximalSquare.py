class Solution:
    def maximalSquare(self, matrix):
        maxNum = float("-inf")
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1 
                    maxNum = max(maxNum, dp[i][j])
        return maxNum * maxNum

    def maximalSquareOptimized(self,matrix):
        maxNum = float('-inf')
        # we only need two rows, each that span the length of the matrix
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(2)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[1][j] = min(dp[1][j-1], dp[0][j-1], dp[0][j]) + 1
                    maxNum = max(maxNum, dp[1][j])
            dp[0] = [i for i in dp[1]] 
            dp[1] = [0 for _ in range(len(matrix[0]))]
        return maxNum
   
one = Solution()
print(one.maximalSquareOptimized([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
