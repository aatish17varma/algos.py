class Solution:
    def largestSumOfAverages(self, A,K) -> float:
        dp = [[None for _ in range(len(A))] for _ in range(K)]
        total = 0
        for i in range(len(dp[0]]):
            total += A[i]
            dp[0][i] = (total) / (i + 1)
    
        for j in range(len(dp)):
            dp[j][0] = A[0]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + A[j])

        print(dp)
        return dp[-1][-1]


