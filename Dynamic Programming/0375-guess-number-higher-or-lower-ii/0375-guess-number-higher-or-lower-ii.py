class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0]*(n+2) for _ in range(n+2)]

        for length in range(2,n+2):
            for left in range(1, n-length+2):
                right = left+length-1
                dp[left][right] = float("inf")

                for guess in range(left, right+1):
                    cost = guess + max(dp[left][guess-1], dp[guess+1][right])
                    dp[left][right] = min(dp[left][right],cost)
        return dp[1][n]
